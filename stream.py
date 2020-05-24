from robot_base import RobotBase


class Stream(RobotBase):
    """
    3.2.15 视频流控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id72
    """

    def set_on(self):
        """
        3.2.17.1. 视频流开启控制
        """
        cmd = "stream on;"
        return self.ctrl_and_reveive(cmd)

    def set_off(self):
        """
        3.2.17.2. 视频流关闭控制
        """
        cmd = "stream off;"
        return self.ctrl_and_reveive(cmd)
