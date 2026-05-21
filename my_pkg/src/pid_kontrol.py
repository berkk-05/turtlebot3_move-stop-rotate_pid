#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class PIDMesafeKontrol:
    def __init__(self):
        rospy.init_node('pid_distance_controller', anonymous=True)
        self.hiz_yayinci = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.lidar_abone = rospy.Subscriber('/scan', LaserScan, self.lidar_callback)
        
        self.Kp = 0.5
        self.Ki = 0.01
        self.Kd = 0.1
        
        self.hedef_mesafe = 0.3 
        self.anlik_mesafe = 0.0
        self.lidar_aktif = False
        
        self.onceki_hata = 0.0
        self.integral_toplami = 0.0
        self.rate = rospy.Rate(10)
        
        self.gorev_tamamlandi = False

    def lidar_callback(self, veri):
        on_cephe = veri.ranges[0:5] + veri.ranges[355:360]
        gecerli_mesafeler = [m for m in on_cephe if 0.05 < m < 8.0]
        
        if len(gecerli_mesafeler) > 0:
            self.anlik_mesafe = min(gecerli_mesafeler)
            self.lidar_aktif = True

    def pid_dongusu(self):
        hiz_mesaji = Twist()
        zaman_adimi = 0.1
        tolerans = 0.02
        
        while not rospy.is_shutdown():
            if self.gorev_tamamlandi:
                self.rate.sleep()
                continue
                
            if self.lidar_aktif:
                hata = self.anlik_mesafe - self.hedef_mesafe
                
                if abs(hata) < tolerans:
                    hiz_mesaji.linear.x = 0.0
                    hiz_mesaji.angular.z = 0.0
                    self.hiz_yayinci.publish(hiz_mesaji)
                    
                    rospy.loginfo(f"Hedefe Ulaşıldı! Mesafe: {self.anlik_mesafe:.2f}m | Görev Bitti, Sistem Kapatıldı.")
                    
                    self.gorev_tamamlandi = True
                    
                else:
                    P = self.Kp * hata
                    self.integral_toplami += hata * zaman_adimi
                    I = self.Ki * self.integral_toplami
                    turev = (hata - self.onceki_hata) / zaman_adimi
                    D = self.Kd * turev
                    
                    kontrol_ciktisi = P + I + D
                    kontrol_ciktisi = max(min(kontrol_ciktisi, 0.22), -0.22)
                    
                    rospy.loginfo(f"Mesafe: {self.anlik_mesafe:.2f}m | Hız: {kontrol_ciktisi:.2f} m/s")
                    
                    hiz_mesaji.linear.x = kontrol_ciktisi
                    hiz_mesaji.angular.z = 0.0
                    self.hiz_yayinci.publish(hiz_mesaji)
                    
                    self.onceki_hata = hata
                
            self.rate.sleep()

if __name__ == '__main__':
    try:
        robot = PIDMesafeKontrol()
        robot.pid_dongusu()
    except rospy.ROSInterruptException:
        pass