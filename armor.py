from robot_base import RobotBase


class Armor(RobotBase):
    """
    3.2.6 装甲板控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id32
    """

    def set_sensitivity(self, value=5):
        """
        3.2.6.1. 装甲板灵敏度控制
        """
        cmd = "armor sensitivity %d;" % value
        return self.ctrl_and_reveive(cmd)

    def get_sensitivity(self):
        """
        3.2.6.2. 装甲板灵敏度获取
        """
        cmd = "armor sensitivity ?;"
        return self.ctrl_and_reveive(cmd)

    def event(self, attr, switch):
        """
        3.2.6.3. 装甲板事件上报控制
        """
        cmd = "armor event %s %s;" % (attr, switch)
        return self.ctrl_and_reveive(cmd)

    def event_hit(self, switch):
        """
        3.2.6.3. 装甲板事件上报控制
        """
        cmd = "armor event hit %s;" % switch
        return self.ctrl_and_reveive(cmd)
