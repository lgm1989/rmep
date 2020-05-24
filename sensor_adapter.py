from robot_base import RobotBase


class SensorAdapter(RobotBase):
    """
    3.2.10 传感器转接板控制
    https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html#id43
    """

    def get_adc(self, id, port):
        """
        3.2.10.1. 传感器转接板 ADC 值获取
        """
        cmd = "sensor_adapter adc id %d port %d;" % (id, port)
        return self.ctrl_and_reveive(cmd)

    def get_io_evel(self, id, port):
        """
        3.2.10.2. 传感器转接板 IO 值获取
        """
        cmd = "sensor_adapter io_level id  %d port %d;" % (id, port)
        return self.ctrl_and_reveive(cmd)

    def get_pulse_eriod(self, id, port):
        """
        3.2.10.3. 传感器转接板 IO 引脚电平跳变时间值获取
        """
        cmd = "sensor_adapter pulse_period id  %d port %d;" % (id, port)
        return self.ctrl_and_reveive(cmd)

    def event_io_level(self, switch):
        """
        3.2.10.4. 传感器转接板事件上报控制
        """
        cmd = "sensor_adapter event io_level %s;" % switch
        return self.ctrl_and_reveive(cmd)
