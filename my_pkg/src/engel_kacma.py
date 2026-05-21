#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class EngeldenKacanRobot:
    def __init__(self):
        rospy.init_node('move_stop_rotate_node', anonymous=True)
        self.hiz_yayinci = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.lidar_abone = rospy.Subscriber('/scan', LaserScan, self.lidar_callback)
        self.hiz_mesaji = Twist()
        
        self.guvenli_mesafe = 0.5
        self.ileri_hiz = 0.2
        self.donus_hizi = 0.2
        
        rospy.loginfo("Kör noktalar kapatıldı. Engelden Kaçma Başladı...")

    def lidar_callback(self, veri):
        sol_taraf = veri.ranges[0:40]
        sag_taraf = veri.ranges[320:360]
        on_cephe = sol_taraf + sag_taraf
        
        gecerli_mesafeler = [mesafe for mesafe in on_cephe if 0.05 < mesafe < 8.0]
        
        if len(gecerli_mesafeler) > 0:
            en_yakin_engel = min(gecerli_mesafeler)
        else:
            en_yakin_engel = float('inf')
            
        if en_yakin_engel > self.guvenli_mesafe:
            self.hiz_mesaji.linear.x = self.ileri_hiz
            self.hiz_mesaji.angular.z = 0.0
        else:
            self.hiz_mesaji.linear.x = 0.0
            self.hiz_mesaji.angular.z = self.donus_hizi
            
        self.hiz_yayinci.publish(self.hiz_mesaji)

if __name__ == '__main__':
    try:
        EngeldenKacanRobot()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass