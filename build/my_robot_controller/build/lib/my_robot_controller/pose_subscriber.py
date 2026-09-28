#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriber(Node):

    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.callback, 10)

    def callback(self, massage: Pose):
        self.get_logger().info("(" + str(massage.x) + ", " + str(massage.y) + ")")

def main():
    rclpy.init()
    node = PoseSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()