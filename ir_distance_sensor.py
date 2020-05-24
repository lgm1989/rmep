from robot_base import RobotBase


class IrDistanceSensor(RobotBase):
    """
    3.2.11 红外深感传感器控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id47
    """

    def set_measure(self, switch):
        """
        3.2.11.1. 红外深度传感器开关控制
        """
        cmd = "ir_distance_sensor measure %s;" % switch
        return self.ctrl_and_reveive(cmd)

    def get_distance(self, id):
        """
        3.2.11.2. 红外深度传感器距离获取
        """
        cmd = "ir_distance_sensor distance %d ?;" % id
        return self.ctrl_and_reveive(cmd)
