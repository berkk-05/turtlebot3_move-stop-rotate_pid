#include "ros/ros.h"
#include <turtlesim/Pose.h> 

void konumOku(const turtlesim::Pose::ConstPtr& msg)
{
  ROS_INFO("Anlik Konum -> X: [%.2f], Y: [%.2f], Aci: [%.2f]", msg->x, msg->y, msg->theta);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "turtle_konum_node");
  ros::NodeHandle nh;

  ros::Subscriber konum_abonesi = nh.subscribe("/turtle1/pose", 10, konumOku);

  ROS_INFO("Konum dinleniyor...");

  ros::spin(); 

  return 0;
}