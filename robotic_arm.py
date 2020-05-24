from robot_base import RobotBase


class RoboticArm(RobotBase):
    """
    3.2.13 机械臂控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id55
    """

    def set_move(self, x, y):
        """
        3.2.13.1. 机械臂相对位置运动控制
        """
        cmd = "robotic_arm move x %f y %f;" % (x, y)
        return self.ctrl_and_reveive(cmd)

    def set_moveto(self, x, y):
        """
        3.2.13.2. 机械臂绝对位置运动控制
        """
        cmd = "robotic_arm moveto x %f y %f;" % (x, y)
        return self.ctrl_and_reveive(cmd)

    def set_recenter(self):
        """
        3.2.13.3. 机械臂回中控制
        """
        cmd = "robotic_arm recenter;"
        return self.ctrl_and_reveive(cmd)

    def set_stop(self):
        """
        3.2.13.4. 机械臂停止运动控制
        """
        cmd = "robotic_arm stop;"
        return self.ctrl_and_reveive(cmd)

    def get_position(self):
        """
        3.2.13.5. 机械臂绝对位置查询
        """
        cmd = "robotic_arm position ?;"
        return self.ctrl_and_reveive(cmd)
