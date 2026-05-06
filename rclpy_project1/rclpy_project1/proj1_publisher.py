import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import Int32

class RclypyProj_Publisher(Node):
  def __init__(self):
    super().__init__('proj1_publisher')
    qos_profile = QoSProfile(depth=10)
    self.proj1_publisher = self.create_publisher(Int32, 'project1', qos_profile)
    self.timer = self.create_timer(1, self.publish_proj1_msg)
    self.count = 0
  def publish_proj1_msg(self):
    msg = Int32()
    msg.data = self.count
    self.proj1_publisher.publish(msg)
    self.get_logger().info('Published message: {0}'.format(msg.data))
    self.count += 1

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
