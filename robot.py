from robot_base import RobotBase

class Robot(RobotBase):
    """
    3.2.2 机器人控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id4
    """

    def set_mode(self, mode):
        """
        3.2.2.1. 机器人运动模式控制
        """
        cmd = "robot mode %d;" % mode
        return self.ctrl_and_reveive(cmd)

    def get_mode(self):
        """
        3.2.2.2. 机器人运动模式获取
        """
        cmd = "robot mode ?;"
        return self.ctrl_and_reveive(cmd)

    def get_battery(self):
        """
        3.2.2.3. 机器人剩余电量获取
        """
        cmd = "robot battery ?;"
        return self.ctrl_and_reveive(cmd)
