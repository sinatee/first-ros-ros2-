#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.circle_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.send_velocity)
        self.get_logger().info("Drawing a Circle")

    def send_velocity(self):
        massage = Twist()
        massage.linear.x = 2.0
        massage.angular.z = 1.0
        self.circle_publisher.publish(massage)

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
 
    rclpy.shutdown()

if __name__ == '__main__':
    main();