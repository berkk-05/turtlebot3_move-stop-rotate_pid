#include "ros/ros.h"
#include <geometry_msgs/Twist.h> 

int main(int argc, char **argv)
{
  ros::init(argc, argv, "turtle_kontrol_node");
  ros::NodeHandle nh;

  ros::Publisher hiz_yayinci = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);

  ros::Rate dongu_hizi(10);

  geometry_msgs::Twist hiz_mesaji;

  ROS_INFO("Hareket Gonderiliyor...");

  while (ros::ok())
  {
    hiz_mesaji.linear.x = 2.0; 
    hiz_mesaji.angular.z = 0.0; 
    hiz_yayinci.publish(hiz_mesaji);
    ros::Duration(1.0).sleep(); 

    hiz_mesaji.linear.x = 0.0; 
    hiz_mesaji.angular.z = 1.5708; 
    hiz_yayinci.publish(hiz_mesaji);
    ros::Duration(1.0).sleep(); 

    ros::spinOnce();
    dongu_hizi.sleep();
  }

  return 0;
}