import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
from sensor_msgs.msg import LaserScan


class DistanceToTable(Node):
    def __init__(self):
        super().__init__('distance_to_table')
        self._scan_sub = self.create_subscription(msg_type=LaserScan, 
                                                  topic='b_scan',
                                                  callback=self.scan_callback,
                                                  qos_profile=10)
        self.get_logger().info("distance to table node created")
    
    def scan_callback(self, msg):
        self.get_logger().info(f"got scan data {len(msg.ranges)}")

def main():
    rclpy.init()
    navigator = BasicNavigator()
    scan_sub = DistanceToTable()
    rclpy.spin_once(scan_sub)
    #setting the initial pose for the experiment 
    initial_pose = PoseStamped()
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.header.frame_id = 'map'

    initial_pose.pose.position.x = 0.0 
    initial_pose.pose.position.y = 0.0
    
    initial_pose.pose.orientation.z = 0.0 
    initial_pose.pose.orientation.w = 1.0 


    navigator.setInitialPose(initial_pose)

    navigator.waitUntilNav2Active()
    
    #setting the goal podse for the experiment
    goal_pose = PoseStamped()
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.header.frame_id = 'map'
    goal_pose.pose.position.x = 4.0 
    goal_pose.pose.position.y = 0.0
    
    goal_pose.pose.orientation.z = 0.0 
    goal_pose.pose.orientation.w = 1.0 

    print('recived goal')

    navigator.goToPose(goal_pose)



    print('Hi from troy_experiment.')


if __name__ == '__main__':
    main()
