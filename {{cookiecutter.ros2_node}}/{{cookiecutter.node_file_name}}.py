#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node


class {{cookiecutter.node_class_name}}(Node):

    def __init__(self):
        super().__init__("{{cookiecutter.node_name}}")
        self.logger_info("Hello ROS2")

    def logger_info(self, text: str):
        self.get_logger().info(text)


def main(args=None):
    rclpy.init(args=args)
    node = {{cookiecutter.node_class_name}}()
    try:
        rclpy.spin(node)  # will hold/keep alive node
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
