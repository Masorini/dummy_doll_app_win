from dynamixel_sdk import *
from backend.services.dxl_com_interface import DXLComInterface

#Control table address
ADDR_TORQUE_ENABLE          = 64
ADDR_GOAL_POSITION          = 116
ADDR_PRESENT_POSITION       = 132
ADDR_PRESENT_TEMPERATURE    = 146

DXL_MINIMUM_POSITION_VALUE  = 0         # Refer to the Minimum Position Limit of product eManual
DXL_MAXIMUM_POSITION_VALUE  = 4095      # Refer to the Maximum Position Limit of product eManual

#Definition of value
TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE  = 0                 # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE  = 4095              # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 20                # Dynamixel moving status threshold

#Unit
POSITION_UNIT               = 0.088

class ServoManager():
    AUTO_MANAGE_COM_ENABLED = True
    def __init__(self, id):
        self.id = id
        self.present_position = 0
        self.present_temperature = 0
        self.is_enable = False # ping online
        self.is_moving = False
        self.dxl_interface = DXLComInterface()
        pass

    def auto_manage_com(func):
        def wrapper(self, *args, **kwargs):
            if(ServoManager.AUTO_MANAGE_COM_ENABLED):
                self.dxl_interface.com_prepare()
                result = func(self, *args, **kwargs)
                self.dxl_interface.com_close()
                return result
            else:
                return func(self, *args, **kwargs)
        return wrapper

    @auto_manage_com
    def get_cur_pos(self):
        return self.dxl_interface.read_4_byte_tx_rx(self.id, ADDR_PRESENT_POSITION)

    @auto_manage_com
    def set_goal_pos(self, pos: int):
        assert(pos >= 0 and pos <= 360)
        pos_rot = round(pos / POSITION_UNIT)
        self.dxl_interface.write_4_byte_tx_rx(self.id, ADDR_GOAL_POSITION, pos_rot)

    @auto_manage_com
    def get_cur_temp(self):
        return self.dxl_interface.read_1_byte_tx_rx(self.id, ADDR_PRESENT_TEMPERATURE)

    @auto_manage_com
    def enable_servo(self):
        self.dxl_interface.write_1_byte_tx_rx(self.id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)

    @auto_manage_com
    def disable_servo(self):
        self.dxl_interface.write_1_byte_tx_rx(self.id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)

    def get_moving(self):
        pass