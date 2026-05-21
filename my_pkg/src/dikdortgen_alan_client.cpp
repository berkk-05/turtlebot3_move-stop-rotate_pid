#include "ros/ros.h"
#include "my_pkg/dikdortgen_alan.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "dikdortgen_alan_client");
  
  // Terminalden 2 adet sayı girilip girilmediğini kontrol ediyoruz
  if (argc != 3)
  {
    ROS_INFO("Kullanim: rosrun my_pkg dikdortgen_alan_client X Y");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<my_pkg::dikdortgen_alan>("dikdortgen_alan");
  
  my_pkg::dikdortgen_alan srv;
  
  // Terminalden girilen string argümanları float (double) formatına çeviriyoruz
  srv.request.en = atof(argv[1]);
  srv.request.boy = atof(argv[2]);

  // Servisi çağırıyoruz
  if (client.call(srv))
  {
    ROS_INFO("Hesaplanan Alan: %f", srv.response.alan);
  }
  else
  {
    ROS_ERROR("dikdortgen_alan servisi cagrilamadi!");
    return 1;
  }

  return 0;
}