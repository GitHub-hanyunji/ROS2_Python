from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_ros2',     # 패키지 이름
            executable='sub',          # 실행파일 이름
            name='camsub_wsl_13',      # 노드 이름
            #arguments=['--ros-args', '--log-level', 'info']
            output='screen',
        ),
        Node(  
            package='dxl_wsl',        # 패키지 이름
            executable='pub',         # 실행파일 이름
            name='node_dxlpub',       # 노드 이름
            prefix='xterm -e',        # xterm 사용 -> launch 파일에서 키보드입력받기 위해 사용
            output='screen',
            #ros_arguments=['--log-level', 'warn']
        ),
    ])
