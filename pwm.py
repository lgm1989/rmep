from robot_base import RobotBase


class PWM(RobotBase):
    """
    3.2.8 PWM控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#pwm
    """

    def set_pwm_value(self, port_mask, value):
        """
        3.2.8.1. PWM 输出占空比控制
        """
        cmd = "pwm value %d %f;" % (port_mask, value)
        return self.ctrl_and_reveive(cmd)

    def set_pwm_freq(self, port_mask, value):
        """
        3.2.8.2. PWM 输出频率控制
        """
        cmd = "pwm value %d %d;" % (port_mask, value)
        return self.ctrl_and_reveive(cmd)
