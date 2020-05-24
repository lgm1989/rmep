from robot_base import RobotBase


class LED(RobotBase):
    """
    3.2.9 LED控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#led
    """

    def set_control_comp(self, led_id, r_value, g_value, b_value, effect):
        """
        3.2.9.1. LED 灯效控制
        """
        cmd = "led control comp %s r %d g %d b %d effect %s;" % (
            led_id, r_value, g_value, b_value, effect)
        return self.ctrl_and_reveive(cmd)
