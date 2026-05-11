from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # camera pub 
        Node(
            package='camera_ros2',     # 패키지 이름
            executable='pub',          # 실행파일 이름
            name='campub',             # 노드명
            output='screen',
        ),
        # dxl sub 구동
        Node(
            package='dxl_nano',       # 패키지 이름
            executable='sub',         # 실행파일 이름
            name='node_dxlsub',       # 노드명
            output='screen',
        )
    ])
