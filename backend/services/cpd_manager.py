from dynamixel_sdk import *
from backend.services.servo_manager import ServoManager

SERVO_NUM = 16

class CPDManager():
    def __init__(self):
        self.servo_dict: dict[str, ServoManager] = {}
        self.cpd_power_on = False
        self.cpd_enable = False
        self.__init_servo_dict()
        self.joints = self.servo_dict.keys()
        self.cur_pos = {}
        pass

    def enable_all_servo(self):
        for servo in self.servo_dict.values():
            servo.enable_servo()

    def disable_all_servo(self):
        for servo in self.servo_dict.values():
            servo.disable_servo()

    def get_cur_temp(self, id: int=None, joint: str=None):
        if(id != None and joint != None):
            assert(self.servo_dict[joint].id == id)
        if(id != None):
            servo = self.get_servo_by_id(id)
        elif(joint != None):
            servo = self.servo_dict[joint]
        else:
            raise Exception("ID和Joint不能同时为空")
        return servo.get_cur_temp()

    def get_all_pos(self) -> dict[str, int]:
        self.cur_pos = {}
        for joint in self.servo_dict.keys():
            pos = self.get_pos(joint=joint)
            self.cur_pos[joint] = pos
        return self.cur_pos

    def get_pos(self, id: int=None, joint: str=None):
        '''
        id:     the id of target servo;
        joint:  the name of target servo like "摆头"

        at least one of id and joint exists;
        if id and joint both exist, they must match or there will raise an exception
        '''
        if(id != None and joint != None):
            assert(self.servo_dict[joint].id == id)
        if(id != None):
            servo = self.get_servo_by_id(id)
        elif(joint != None):
            servo = self.servo_dict[joint]
        else:
            raise Exception("ID和Joint不能同时为空")
        return servo.get_cur_pos()

    def set_pos(self, id: int=None, joint: str=None, pos: int=None):
        if(id != None and joint != None):
            assert(self.servo_dict[joint].id == id)
        if(id != None):
            servo = self.get_servo_by_id(id)
        elif(joint != None):
            servo = self.servo_dict[joint]
        else:
            raise Exception("ID和Joint不能同时为空")
        return servo.set_goal_pos(pos)

    def __init_servo_dict(self):
        '''
        init the servo_dict
        '''
        self.servo_dict['摆头'] = ServoManager(1)
        # self.servo_dict['抬头'] = ServoManager(2)
        # self.servo_dict['左肩前摆'] = ServoManager(3)
        # self.servo_dict['左肩侧摆'] = ServoManager(4)
        # self.servo_dict['左肘'] = ServoManager(5)
        # self.servo_dict['右肩前摆'] = ServoManager(6)
        # self.servo_dict['右肩侧摆'] = ServoManager(7)
        # self.servo_dict['右肘'] = ServoManager(8)
        # self.servo_dict['左髋前摆'] = ServoManager(9)
        # self.servo_dict['左髋旋转'] = ServoManager(10)
        # self.servo_dict['左膝'] = ServoManager(11)
        # self.servo_dict['右髋前摆'] = ServoManager(12)
        # self.servo_dict['右髋旋转'] = ServoManager(13)
        # self.servo_dict['右膝'] = ServoManager(14)
        # self.servo_dict['呼吸'] = ServoManager(15)
        # self.servo_dict['心跳'] = ServoManager(16)

    def get_servo_by_id(self, id):
        for servo in self.servo_dict.values():
            if servo.id == id:
                return servo
        raise Exception('请检查传入ID是否正确')

cpd = CPDManager()