from robot_base import RobotBase


class Blaster(RobotBase):
    """
    3.2.5 发射器控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id18
    """

    def set_bead(self, num):
        """
        3.2.5.1. 发射器单次发射量控制
        """
        cmd = "blaster bead %d;" % num
        return self.ctrl_and_reveive(cmd)

    def set_fire(self):
        """
        3.2.5.2. 发射器发射控制
        """
        cmd = "blaster fire;"
        return self.ctrl_and_reveive(cmd)

    def get_bead(self):
        """
        3.2.5.3. 发射器单次发射量获取
        """
        cmd = "blaster bead ?;"
        return self.ctrl_and_reveive(cmd)
