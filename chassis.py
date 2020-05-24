from robot_base import RobotBase

class Chassis(RobotBase):
    """
    3.2.3 底盘控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id8
    """

    def set_speed(self, x, y, z):
        """
        3.2.3.1. 底盘运动速度控制
        """
        cmd = "chassis speed x %f y %f z %f;" % (x, y, z)
        return self.ctrl_and_reveive(cmd)

    def set_wheel(self, w1, w2, w3, w4):
        """
        3.2.3.2. 底盘轮子速度控制
        """
        cmd = "chassis wheel w1 %d w2 %d w3 %d w4 %d;" % (w1, w2, w3, w4)
        return self.ctrl_and_reveive(cmd)

    def set_move(self, x=0, y=0, z=0, vxy=0, vz=0):
        """
        3.2.3.3. 底盘相对位置控制
        """
        cmd = "chassis move"
        if x:
            cmd += " x %f" % x
        if y:
            cmd += " y %f" % y
        if z:
            cmd += " z %d" % z
        if vxy:
            cmd += " vxy %f" % vxy
        if vz:
            cmd += " vz %f" % vz
        cmd += ";"
        return self.ctrl_and_reveive(cmd)

    def get_speed(self):
        """
        3.2.3.4. 底盘速度获取
        """
        cmd = "chassis speed ?;"
        return self.ctrl_and_reveive(cmd)

    def get_position(self):
        """
        3.2.3.5. 底盘位置获取
        """
        cmd = "chassis position ?;"
        return self.ctrl_and_reveive(cmd)

    def get_attitude(self):
        """
        3.2.3.6. 底盘姿态获取
        """
        cmd = "chassis attitude ?;"
        return self.ctrl_and_reveive(cmd)

    def get_status(self):
        """
        3.2.3.7. 底盘状态获取
        """
        cmd = "chassis status ?;"
        return self.ctrl_and_reveive(cmd)

    def push(self, attr, switch, freq=5):
        """
        3.2.3.8. 底盘信息推送控制
        """
        freq_name = attr[0:1] + "freq"
        cmd = "chassis push %s %s %s %d;" % (attr, switch, freq_name, freq)
        return self.ctrl_and_reveive(cmd)

    def push_position(self, switch, freq=5):
        """
        3.2.3.8. 底盘信息推送控制（获取位置）
        """
        cmd = "chassis push position %s pfreq %d;" % (switch, freq)
        return self.ctrl_and_reveive(cmd)

    def push_attitude(self, switch, freq=5):
        """
        3.2.3.8. 底盘推送信息数据（获取属性）
        """
        cmd = "chassis push attitude %s afreq %d;" % (switch, freq)
        return self.ctrl_and_reveive(cmd)

    def push_status(self, switch, freq=5):
        """
        3.2.3.8. 底盘推送信息数据（获取状态）
        """
        cmd = "chassis push status %s sfreq %d;" % (switch, freq)
        return self.ctrl_and_reveive(cmd)

    def push_freq_all(self, freq=5):
        """
        3.2.3.8. 底盘推送信息数据（获取属性）
        """
        #error
        cmd = "chassis push freq %d;" % freq
        return self.ctrl_and_reveive(cmd)
