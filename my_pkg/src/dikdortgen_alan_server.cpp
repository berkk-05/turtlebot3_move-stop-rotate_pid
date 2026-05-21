#include "ros/ros.h"
#include "my_pkg/dikdortgen_alan.h" 
bool alan_hesapla(my_pkg::dikdortgen_alan::Request  &req,
                  my_pkg::dikdortgen_alan::Response &res)
{
  
  res.alan = req.en * req.boy;
  
  ROS_INFO("Istek alindi: en=%f, boy=%f", req.en, req.boy);
  ROS_INFO("Gonderilen cevap (Alan): [%f]", res.alan);
  
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "dikdortgen_alan_server");
  ros::NodeHandle n;

  // servis başlat
  ros::ServiceServer service = n.advertiseService("dikdortgen_alan", alan_hesapla);
  ROS_INFO("Dikdortgen alani hesaplamaya hazir.");
  
  ros::spin(); 

  return 0;
}