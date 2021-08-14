# cookiecutter_ros2_python_node
Cookiecutter project which creates a Node template file


## How to use
- install cookiecutter `pip install cookiecutter`
- then
- `cookiecutter https://github.com/FelixTheC/cookiecutter_ros2_python_node.git`
- you will then see `node_file_name [new_node]:` in the terminal
  - the value inside of the `[..]` is the default value

| Parameter         | Description                       |
| :-------------     |   :-------------:                 |
|node_file_name     |   the filename of the new node    |
|node_class_name    |   the class name of the Node (the default value should fit)|
|node_name          |   the value inside of `super().__init__(<node_name>)`|
|ros2_node          |   don't change the default value  |
|final_destination  |   the path to where put your new node file (see default for more informations)|


### Example file with only default values
- filename `new_node.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node


class NewNode(Node):

  def __init__(self):
    super().__init__("new_node")
    self.logger_info("Hello ROS2")

  def logger_info(self, text: str):
    self.get_logger().info(text)


def main(*args):
  rclpy.init(args=args)
  node = NewNode()
  try:
    rclpy.spin(node)  # will hold/keep alive node
  finally:
    rclpy.shutdown()


if __name__ == '__main__':
  main()

```
