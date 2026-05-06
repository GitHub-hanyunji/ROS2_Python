import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Twist

class RclypyProj_Publisher(Node):
  def __init__(self):
    super().__init__('proj3_publisher')
    qos_profile = QoSProfile(depth=10)
    self.proj3_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', qos_profile)
    self.timer = self.create_timer(1, self.publish_proj3_msg)
  def publish_proj3_msg(self):
    msg = Twist()
    c= str(input("f->전진, b->후진, l->좌회전, r->우회전: "))
    match c:
      case "f":
        msg.linear.x=2.0
        msg.angular.z = 0.0    
      case "b":
        msg.linear.x=-2.0
        msg.angular.z = 0.0
      case "l":
        msg.linear.x=0.0
        msg.angular.z = 2.0
      case "r":
        msg.linear.x=0.0
        msg.angular.z = -2.0
      case _:
        msg.linear.x=0.0
        msg.angular.z = 0.0
      
    self.proj3_publisher.publish(msg)
    self.get_logger().info('Published message: x={0}, y={1}, z={2}'.format(msg.linear.x, msg.linear.y, msg.linear.z))

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
