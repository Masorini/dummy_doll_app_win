from dynamixel_sdk import *
from servoManager import ServoManager

SERVO_NUM = 16

class CPDManager():
    def __init__(self):
        self.servo_list = []
        self.cpd_power_on = False
        self.cpd_enable = False
        self.init_servo_list()
        pass

    def init_servo_list(self):
        for i in range(SERVO_NUM):
            self.servo_list.append(ServoManager(i))