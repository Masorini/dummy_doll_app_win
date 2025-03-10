from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import pyqtSlot
from backend.services.servo_manager import ServoManager


class OfflineController(QObject):
    def __init__(self):
        self.servo = ServoManager(1) # TODO: just for test, change in the future
        pass

    @pyqtSlot()
    def run(self):
        self.servo.enable_servo()
        pass

    def stop(self):
        pass

    def Radios(self):
        pass

