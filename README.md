# rmep
RoboMaster-SDK二次封装

## 说明

此代码依据原生[RoboMaster-SDK](https://github.com/dji-sdk/RoboMaster-SDK)的SDK连接代码，以及[sdk文档](https://github.com/dji-sdk/RoboMaster-SDK)和命令行进行了命令的二次封装，方便开发人员进行功能测试和开发。

## 环境

- RoboMaster-EP
- mac和jetson nano都经过测试
- python3.6

## 二次封装原则

- 使用原生sdk中的连接ep代码，[robot_connection.py](https://github.com/dji-sdk/RoboMaster-SDK/blob/master/sample_code/RoboMasterEP/connection/network/robot_connection.py)

- 控制代码入口为robot_control.py，通过RobotControl类实例化进行控制
- 依据sdk文档中的说明，对每一项进行了类的封装，文件名为各个控制项的英文名称，与文档中控制命令第一项保持一致。
- 对于各个控制项中各个方法的封装：
  - 设置类型对应类的方法中的set_***()，即返回数据为ok的控制方法；_
  - _获取信息类型对应类的方法中的get_***()，即会返回ep状态数据；
  - 参数与命令中的变量保持一致；
  - push方法命名为push() ，(之前为了方便对每一个push功能进行了拆分，后面可能会删除)；
  - event方法命名为event()；
  - 接受push消息使用recv_push_data()，接收event消息使用recv_event_data()，如果要一直接收需要while True循环或者直接使用recv_push_data_forever和recv_event_data_forever()

- 如果需要新增控制项，需要新增一个类，并在RobotControl类中的构造函数中增加控制项的实例化成员变量；
- 如果需要新增或者修改控制项中的具体方法，需要在相应的类中进行新增或修改；

## 测试

使用路由器连接方式，可执行test.py进行功能测试，因为经历有限，未对全部功能进行测试，如下为测试情况。

| 测试项             | 测试结果 | 备注                                             |
| ------------------ | :------- | ------------------------------------------------ |
| 机器人控制         | 通过     |                                                  |
| 底盘控制           | 通过     | *chassis push freq 10*；命令成功，返回数据为None |
| 云台控制           | 通过     |                                                  |
| 发射器控制         | 通过     |                                                  |
| 装甲板控制         | 通过     |                                                  |
| 声音识别控制       | 通过     |                                                  |
| PWM控制            | 未测试   |                                                  |
| LED控制            | 通过     |                                                  |
| 传感器转接板控制   | 未测试   |                                                  |
| 红外深度传感器控制 | 通过     |                                                  |
| 舵机控制           | 通过     |                                                  |
| 智能识别功能控制   | 未测试   |                                                  |
| 相机控制           | 通过     |                                                  |
| 视频流控制         | 通过     | 未进行视频流解码测试                             |
| 音频流控制         | 通过     | 未进行音频流解码测试                             |
|                    |          |                                                  |

## TODO

对剩下的功能进行测试，对返回值进行更细致的处理
