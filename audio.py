from robot_base import RobotBase


class Audio(RobotBase):
    """
    3.2.18 音频流控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id75
    """

    def set_on(self):
        """
        3.2.18.1. 音频流开启控制
        """
        cmd = "audio on;"
        return self.ctrl_and_reveive(cmd)

    def set_off(self):
        """
        3.2.18.2. 音频流关闭控制
        """
        cmd = "audio off;"
        return self.ctrl_and_reveive(cmd)
