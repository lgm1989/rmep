import threading
import time
from robot_control import RobotControl
from robot_enum import *

rc = RobotControl()
rc.start()

#启两个线程持续接收push和event消息
event_thread = threading.Thread(target = rc.recv_event_data_forever)
push_thread = threading.Thread(target = rc.recv_push_data_forever)

#机器人控制测试
rc.robot.set_mode(mode_enum.chassis_lead)
rc.robot.get_mode()
rc.robot.get_battery()

#底盘控制测试
rc.chassis.set_speed(0.1, 0.1, 1)
rc.chassis.set_wheel(100, 12, 20, 11)
rc.chassis.set_move(x = 0.1, y = 0.2)
rc.chassis.get_speed()
rc.chassis.get_position()
rc.chassis.get_attitude()
rc.chassis.get_status()
# rc.chassis.push("attitude", switch_enum.on)
#接收一次push信息，如果想要一直接收请用while True
# rc.chassis.recv_push_data()
#推送所有数据命令成功，但是返回数据为None
rc.chassis.push_freq_all()
while True:
    rc.chassis.recv_push_data()

#云台控制测试
rc.gimbal.set_speed(1, 1)
rc.gimbal.set_move(p = 10)
rc.gimbal.set_moveto(10, -20, 0.1)
rc.gimbal.set_suspend()
rc.gimbal.set_resume()
rc.gimbal.set_recenter()
rc.gimbal.get_attitude()
rc.gimbal.push("attitude", switch_enum.on)
rc.gimbal.recv_push_data()

#发射器控制测试
rc.blaster.set_bead(3)
rc.blaster.set_fire()
rc.blaster.get_bead()

#装甲控制测试
rc.armor.set_sensitivity(10)
rc.armor.get_sensitivity()
rc.armor.event_hit(switch_enum.on)
#持续接收时间请用while True
rc.armor.recv_event_data()

#声音识别控制测试
rc.sound.event_applause(switch_enum.on)
rc.sound.recv_event_data()

#pwm未测试

#led控制测试
rc.led.set_control_comp(led_comp_enum.top_all, 255, 0, 0, led_effect_enum.solid)

#传感器未测试

#红外深度传感器测试
rc.ir_distance_sensor.set_measure(switch_enum.on)
rc.ir_distance_sensor.get_distance(1)

#舵机控制测试
rc.servo.set_angle(1, 20)
time.sleep(2)
rc.servo.set_speed(1, 20)
time.sleep(2)
rc.servo.set_stop()
rc.servo.get_angle(1)

#机械臂控制测试
rc.robotic_arm.set_move(5, 5)
rc.robotic_arm.set_moveto(5, 5)
rc.robotic_arm.set_recenter()
rc.robotic_arm.set_stop()
rc.robotic_arm.get_position()

#机械爪控制测试
rc.robotic_gripper.set_open(4)
rc.robotic_gripper.set_close(1)
rc.robotic_gripper.get_status()

#智能识别功能控制未测试

#相机控制
rc.camera.set_exposure(camera_ev_enum.small)

#视频流开关测试
rc.stream.set_on()
rc.stream.set_off()

#音频流开关测试
rc.audio.set_on()
rc.audio.set_off()

#启动监听线程
event_thread.start()
push_thread.start()
event_thread.join()
push_thread.join()

rc.stop()
rc.close()