from robot_base import RobotBase


class AI(RobotBase):
    """
    3.2.15 智能识别功能控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id65
    """

    def set_atrribute(self, line_color, marker_color, marker_dist=0.5):
        """
        3.2.15.1. 智能识别功能属性控制
        """
        cmd = "AI attribute %s %s %f;" % (line_color, marker_color, marker_dist)
        return self.ctrl_and_reveive(cmd)

    def push(self, attr, switch):
        """
        3.2.15.2. 智能识别功能推送控制
        """
        cmd = "AI push %s %s;" % (attr, switch)
        return self.ctrl_and_reveive(cmd)

    def push_person(self, switch):
        """
        3.2.15.2. 智能识别功能推送控制
        """
        cmd = "AI push person %s;" % switch
        return self.ctrl_and_reveive(cmd)

    def push_gesture(self, switch):
        """
        3.2.15.2. 智能识别功能推送控制
        """
        cmd = "AI push gesture %s;" % switch
        return self.ctrl_and_reveive(cmd)

    def push_marker(self, switch):
        """
        3.2.15.2. 智能识别功能推送控制
        """
        cmd = "AI push marker %s;" % switch
        return self.ctrl_and_reveive(cmd)

    def push_line(self, switch):
        """
        3.2.15.2. 智能识别功能推送控制
        """
        cmd = "AI push line %s;" % switch
        return self.ctrl_and_reveive(cmd)

    def push_robot(self, switch):
        """
        3.2.15.2. 智能识别功能推送控制
        """
        cmd = "AI push robot %s;" % switch
        return self.ctrl_and_reveive(cmd)
