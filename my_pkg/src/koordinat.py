#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def move_to_goal(x, y, w):
    # move_base action server'ı için bir istemci oluşturuyoruz
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    
    # Sunucunun ayağa kalkmasını bekliyoruz
    client.wait_for_server()
    
    # Hedef (goal) objesini oluşturuyoruz
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    
    # Hedefin X ve Y koordinatları
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    
    # Hedefteki yönelim (Quaternion formatında, w=1 düz bakmasını sağlar)
    goal.target_pose.pose.orientation.w = w
    
    # Hedefi sunucuya gönderiyoruz
    client.send_goal(goal)
    
    # Robotun hedefe ulaşmasını bekliyoruz
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action sunucusu yanıt vermiyor!")
        rospy.signal_shutdown("Action sunucusu yanıt vermiyor!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        # ROS düğümünü başlatıyoruz
        rospy.init_node('waypoint_navigator_node')
        
        # Gitmek istediğiniz 5 noktanın (X, Y, W) koordinat listesi

        waypoints = [
            (0.0, 1.5, 1.0),  # 1. Nokta
            (0.5, 0.5, 1.0),  # 2. Nokta
            (1.5, 0.0, 1.0),  # 3. Nokta
            (0.5, -0.5, 1.0), # 4. Nokta
            (-0.5, 0.0, 1.0)   # 5. Nokta 
        ]
        
        for idx, point in enumerate(waypoints):
            rospy.loginfo("{}. Noktaya gidiliyor: X={}, Y={}".format(idx+1, point[0], point[1]))
            
            # Fonksiyonu çağır ve robotu gönder
            result = move_to_goal(point[0], point[1], point[2])
            
            if result:
                rospy.loginfo("{}. Noktaya başarıyla ulaşıldı!\n".format(idx+1))
                rospy.sleep(1) # Diğer hedefe geçmeden önce 1 saniye bekle
                
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigasyon testi iptal edildi.")
