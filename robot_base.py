class RobotBase():
    """
    robot基类，用于处理与设备交互命令
    """

    def __init__(self, conn):
        self.conn = conn

    def ctrl_and_reveive(self, cmd):
        print('send data to robot : %s' % cmd)
        self.conn.send_data(cmd)
        recv = self.conn.recv_ctrl_data(5)
        print("recv data from robot : %s" % recv)
        return recv.decode("utf-8")[0:-1]

    def recv_push_data(self):
        recv = self.conn.recv_push_data(5)
        print("recv data from robot : %s" % recv)
        return recv

    def recv_event_data(self):
        recv = self.conn.recv_event_data(5)
        print("recv data from robot : %s" % recv)
        return recv
