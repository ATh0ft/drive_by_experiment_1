import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator


def main():
    rclpy.init()
    navigator = BasicNavigator()
    
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
