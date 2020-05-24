from robot_base import RobotBase


class RoboticGripper(RobotBase):
    """
    3.2.14 机械爪控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id64
    """

    def set_open(self, level):
        """
        3.2.14.1. 机械爪张开运动控制
        """
        cmd = "obotic_gripper open %d;" % level
        return self.ctrl_and_reveive(cmd)

    def set_close(self, level):
        """
        3.2.14.2. 机械爪关闭运动控制
        """
        cmd = "obotic_gripper close %d;" % level
        return self.ctrl_and_reveive(cmd)

    def get_status(self):
        """
        3.2.14.3. 机械爪开合状态查询
        """
        cmd = "robotic_gripper status ?;"
        return self.ctrl_and_reveive(cmd)
