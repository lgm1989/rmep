from robot_base import RobotBase

class Gimbal(RobotBase):
    """
    3.2.4 云台控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id18
    """

    def set_speed(self, p, y):
        """
        3.2.4.1. 云台运动速度控制
        """
        cmd = "gimbal speed p %f y %f;" % (p, y)
        return self.ctrl_and_reveive(cmd)

    def set_move(self, p=0, y=0, vp=0, vy=0):
        """
        3.2.4.2. 云台相对位置控制
        """
        cmd = "gimbal move"
        if p:
            cmd += " p %f" % p
        if y:
            cmd += " y %f" % y
        if vp:
            cmd += " vp %f" % vp
        if vy:
            cmd += " vy %f" % vy
        cmd += ";"
        return self.ctrl_and_reveive(cmd)

    def set_moveto(self, p=0, y=0, vp=0, vy=0):
        """
        3.2.4.3. 云台绝对位置控制
        """
        cmd = "gimbal moveto"
        if p:
            cmd += " p %f" % p
        if y:
            cmd += " y %f" % y
        if vp:
            cmd += " vp %f" % vp
        if vy:
            cmd += " vy %f" % vy
        cmd += ";"
        return self.ctrl_and_reveive(cmd)

    def set_suspend(self):
        """
        3.2.4.4. 云台休眠控制
        """
        cmd = "gimbal suspend;"
        return self.ctrl_and_reveive(cmd)

    def set_resume(self):
        """
        3.2.4.5. 云台恢复控制
        """
        cmd = "gimbal resume;"
        return self.ctrl_and_reveive(cmd)

    def set_recenter(self):
        """
        3.2.4.6. 云台回中控制
        """
        cmd = "gimbal recenter;"
        return self.ctrl_and_reveive(cmd)

    def get_attitude(self):
        """
        3.2.4.7. 云台姿态获取
        """
        cmd = "gimbal attitude ?;"
        return self.ctrl_and_reveive(cmd)

    def push(self, attr, switch, freq=5):
        """
        3.2.3.8. 底盘信息推送控制
        """
        freq_name = attr[0:1] + "freq"
        cmd = "gimbal push %s %s %s %d;" % (attr, switch, freq_name, freq)
        return self.ctrl_and_reveive(cmd)

    def push_attitude(self, switch, freq=5):
        """
        3.2.4.8. 云台信息推送控制
        """
        cmd = "gimbal push attitude %s afreq %d;" % (switch, freq)
        return self.ctrl_and_reveive(cmd)
