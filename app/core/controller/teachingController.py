from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import pyqtSlot
from backend.services.servoManager import ServoManager

class TeachingController(QObject):
    def __init__(self):
        self.servo = ServoManager(1) # TODO: just for test, change in the future
        pass

    # TODO: just for test, change in the future
    @pyqtSlot()
    def power_on(self):
        print("Received Signal {}".format("power on"))
        self.servo.enable_servo()
        pass

    def power_off(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def read_present_position(self):
        pass

    def stop_read_position(self):
        pass