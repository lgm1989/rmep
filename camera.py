from robot_base import RobotBase


class Camera(RobotBase):
    """
    3.2.16 相机控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id70
    """

    def set_exposure(self, ev_level):
        """
        3.2.16.1. 相机曝光设置
        """
        cmd = "camera exposure %s;" % ev_level
        return self.ctrl_and_reveive(cmd)
