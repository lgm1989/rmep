from robot_connection import RobotConnection
from ai import AI
from armor import Armor
from audio import Audio
from blaster import Blaster
from camera import Camera
from chassis import Chassis
from gimbal import Gimbal
from ir_distance_sensor import IrDistanceSensor
from led import LED
from pwm import PWM
from robot import Robot
from robotic_arm import RoboticArm
from robotic_gripper import RoboticGripper
from sensor_adapter import SensorAdapter
from servo import Servo
from sound import Sound
from stream import Stream


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class RobotControl(Singleton):
    """
    robot主控类，可控制类型为其成员变量
    """
    def __init__(self):
        self.conn = RobotConnection()

        robot_ip = self.conn.get_robot_ip(10)

        if robot_ip:
            print('robot ip: %s'%robot_ip)
            self.conn.update_robot_ip(robot_ip)

        if not self.conn.open():
            print('open fail')
            exit(1)
        self.robot = Robot(self.conn)
        self.chassis = Chassis(self.conn)
        self.gimbal = Gimbal(self.conn)
        self.blaster = Blaster(self.conn)
        self.armor = Armor(self.conn)
        self.sound = Sound(self.conn)
        self.pwm = PWM(self.conn)
        self.led = LED(self.conn)
        self.sensor_dapter = SensorAdapter(self.conn)
        self.ir_distance_sensor = IrDistanceSensor(self.conn)
        self.servo = Servo(self.conn)
        self.robotic_arm = RoboticArm(self.conn)
        self.robotic_gripper = RoboticGripper(self.conn)
        self.stream = Stream(self.conn)
        self.audio = Audio(self.conn)
        self.ai = AI(self.conn)
        self.camera = Camera(self.conn)

    def start(self):
        self.conn.send_data('command;')
        print('send data to robot   : command')
        recv = self.conn.recv_ctrl_data(5)
        print('recv data from robot : %s'%recv)

    def stop(self):
        self.conn.send_data('quit;')
        print('send data to robot   : quit')
        recv = self.conn.recv_ctrl_data(5)
        print('recv data from robot : %s'%recv)
    
    def recv_push_data(self):
        recv = self.conn.recv_push_data(5)
        print("recv data from robot : %s" % recv)
        return recv

    def recv_event_data(self):
        recv = self.conn.recv_event_data(5)
        print("recv data from robot : %s" % recv)
        return recv
    
    def recv_push_data_forever(self):
        while True:
            recv = self.conn.recv_push_data(5)
            if recv:
                print("recv data from robot : %s" % recv)

    def recv_event_data_forever(self):
        while True:
            recv = self.conn.recv_event_data(5)
            if recv:
                print("recv data from robot : %s" % recv)

    def close(self):
        print('ready to close robot connection')
        try:
            self.conn.close()
            print("close robot connecntion sucess!")
        except:
            print("close robot connecntion fail! please check")
