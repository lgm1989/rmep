from robot_base import RobotBase


class Sound(RobotBase):
    """
    3.2.7 声音识别控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id37
    """

    def event(self, attr, switch):
        """
        3.2.7.1. 声音识别事件上报控制
        """
        cmd = "sound event %s %s;" % (attr, switch)
        return self.ctrl_and_reveive(cmd)

    def event_applause(self, switch):
        """
        3.2.7.1. 声音识别事件上报控制
        """
        cmd = "sound event applause %s;" % switch
        return self.ctrl_and_reveive(cmd)
