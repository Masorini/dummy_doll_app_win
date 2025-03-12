from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from backend.services.servo_manager import ServoManager

class RealtimeController(QObject):
    action_selected = pyqtSignal(str)
    breathing_rate_changed = pyqtSignal(int)
    breathing_amplitude_changed = pyqtSignal(int)
    heartbeat_rate_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.breathing_rate = 0
        self.breathing_amplitude = 0
        self.heartbeat_rate = 0
        self.servo = ServoManager(1) # TODO: just for test, change in the future

    @pyqtSlot()
    def power_on(self):
        print("Power on action...")
        # self.servo.enable_servo()

    @pyqtSlot()
    def execute(self):
        print("Executing action...")
        # TODO: Implement execution logic

    @pyqtSlot()
    def stop(self):
        print("Stopping action...")
        # TODO: Implement stop logic

    def set_breathing_rate(self, value: int):
        self.breathing_rate = value
        self.breathing_rate_changed.emit(value)
        print("Set breathing rate to " + str(value))

    def set_breathing_amplitude(self, value: int):
        self.breathing_amplitude = value
        self.breathing_amplitude_changed.emit(value)
        print("Set breathing amplitude to " + str(value))

    def set_heartbeat_rate(self, value: int):
        self.heartbeat_rate = value
        self.heartbeat_rate_changed.emit(value)
        print("Set heartbeat rate to " + str(value))

    def select_action(self, action):
        print(f"Selected action: {action}")
        self.action_selected.emit(action)

    @pyqtSlot()
    def load_configuration(self):
        print("Loading configuration...")
        # TODO: Implement configuration loading logic