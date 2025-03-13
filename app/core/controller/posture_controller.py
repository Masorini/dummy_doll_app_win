from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import pyqtSlot
from backend.services.servo_manager import ServoManager

class PostureController(QObject):
    def __init__(self):
        self.posture_params = {i: 60 for i in range(1, 15)}  # 默认值60
        self.servo = ServoManager(1) # TODO: just for test, change in the future

    @pyqtSlot()
    def power_on(self):
        """Handles powering on the servo."""
        print("Powering on...")

    @pyqtSlot()
    def power_off(self):
        """Handles powering off the servo."""
        print("Powering off...")

    @pyqtSlot()
    def enable(self):
        """Enables the servo."""
        print("Enabling servo...")

    @pyqtSlot()
    def disable(self):
        """Disables the servo."""
        print("Disabling servo...")

    @pyqtSlot()
    def read_posture(self):
        """Reads the current posture of the servo."""
        print(f"Current posture")

    @pyqtSlot()
    def set_zero_position(self):
        """Sets the current posture as the zero position."""
        print("Setting zero position...")

    @pyqtSlot()
    def test_zero_position(self):
        """Tests moving the servo to the zero position."""
        print("Testing zero position...")

    @pyqtSlot()
    def save_to_flash(self):
        """Saves current settings to flash."""
        print("Saving settings to flash...")

    @pyqtSlot(int, int)
    def update_posture_param(self, param_index, value):
        """更新某个姿态参数的数值"""
        if param_index in self.posture_params:
            # self.posture_params[param_index] = value
            print(f"parameter {param_index} update to {value}")

    @pyqtSlot()
    def apply_manual_config(self):
        """将手动配置参数应用到电机"""
        print("apply manual config parameters:", self.posture_params)
        # self.servo.apply_posture_config(self.posture_params)
