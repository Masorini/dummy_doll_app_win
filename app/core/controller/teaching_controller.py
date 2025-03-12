from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import pyqtSlot
from backend.services.servo_manager import ServoManager

class TeachingController(QObject):
    def __init__(self):
        super().__init__()
        self.servo = ServoManager(1)  # TODO: 未来修改 ID

    @pyqtSlot()
    def power_on(self):
        """上电"""
        print("power on...")
        # self.servo.enable_servo()

    @pyqtSlot()
    def power_off(self):
        """断电"""
        print("power off...")

    @pyqtSlot()
    def enable_servo(self):
        """使能"""
        print("enable servo...")

    @pyqtSlot()
    def disable_servo(self):
        """去使能"""
        print("disable servo...")

    @pyqtSlot()
    def read_pos(self):
        print("read pos...")

    @pyqtSlot()
    def stop_read_pos(self):
        print("stop read pos...")

    @pyqtSlot()
    def add_seq(self):
        print("add seq...")

    @pyqtSlot()
    def clear_seq(self):
        print("clear seq...")

    @pyqtSlot()
    def zero_seq(self):
        print("zero seq...")

    @pyqtSlot()
    def generate(self):
        print("generate...")