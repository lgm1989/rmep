from robot_base import RobotBase


class Servo(RobotBase):
    """
    3.2.12 舵机控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id50
    """

    def set_angle(self, id, angle):
        """
        3.2.12.1. 舵机角度控制
        """
        cmd = "servo angle id %d angle %f;" % (id, angle)
        return self.ctrl_and_reveive(cmd)

    def set_speed(self, id, speed):
        """
        3.2.12.2. 舵机速度控制
        """
        cmd = "servo speed id %d speed %f;" % (id, speed)
        return self.ctrl_and_reveive(cmd)

    def set_stop(self):
        """
        3.2.12.3. 舵机停止控制
        """
        cmd = "servo stop;"
        return self.ctrl_and_reveive(cmd)

    def get_angle(self, id):
        """
        3.2.12.4. 舵机角度查询
        """
        cmd = "servo angle id %d ?;" % id
        return self.ctrl_and_reveive(cmd)
