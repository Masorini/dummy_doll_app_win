from dynamixel_sdk import *
from backend.services.dxlComInterface import DXLComInterface

class ServoManager():
    def __init__(self, id):
        self.id = id
        self.present_position = 0
        self.present_temperature = 0
        self.is_enable = False # ping online
        self.is_moving = False
        self.dxl_interface = DXLComInterface()
        pass

    def get_present_position(self):
        pass

    def set_goal_position(self):
        pass

    def get_present_temperature(self):
        pass

    def enable_servo(self):
        self.dxl_interface.ping(self.id)
        pass

    def disable_servo(self):
        pass

    def get_moving(self):
        pass