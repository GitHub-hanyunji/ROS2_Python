import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Vector3

class RclypyProj_Publisher(Node):
  def __init__(self):
    super().__init__('proj2_publisher')
    qos_profile = QoSProfile(depth=10)
    self.proj2_publisher = self.create_publisher(Vector3, 'project2', qos_profile)
    self.timer = self.create_timer(1, self.publish_proj1_msg)
    self.msg = Vector3()
    self.msg.x, self.msg.y, self.msg.z = map(float, input("x y z 입력 (공백으로 구분): ").split())
  def publish_proj1_msg(self):
    self.proj2_publisher.publish(self.msg)
    self.get_logger().info('Published message: x={0}, y={1}, z={2}'.format(self.msg.x, self.msg.y, self.msg.z))

def main(args=None):
  rclpy.init(args=args)
  node = RclypyProj_Publisher()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard Interrupt (SIGINT)')
  finally:
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
  main()
