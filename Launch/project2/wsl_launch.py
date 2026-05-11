from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # pub 노드 1
        Node(
            package='rclpy_project1',
            namespace='rclpy_psub1',
            executable='pub',
            name='proj1_publisher',
        ),
        # pub 노드 2
        Node(
            package='rclpy_project1',
            namespace='rclpy_psub2',
            executable='pub',
            name='proj1_publisher',
        ),
        #sub 노드 1
        Node(
            package='rclpy_project1',
            namespace='rclpy_psub2',
            executable='sub',
            name='proj1_subscriber',
        ),
        # sub 노드 2
        Node(
            package='rclpy_project1',
            namespace='rclpy_psub2',
            executable='sub',
            name='proj1_subscriber',
        ),
    
    ])
