from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from backend.services.servo_manager import ServoManager


class OfflineController(QObject):
    """离线模式控制器"""

    status_updated = pyqtSignal(str)  # 用于更新界面状态

    def __init__(self):
        super().__init__()
        self.servo = ServoManager(1)  # TODO: 未来修改 ID

    @pyqtSlot()
    def power_on(self):
        print("power on...")

    @pyqtSlot()
    def run_action(self):
        print("run action...")
        # self.status_updated.emit("执行中...")

    @pyqtSlot()
    def stop_action(self):
        """停止当前动作"""
        print("stop action...")
        # self.status_updated.emit("已停止")

    @pyqtSlot()
    def load_action(self):
        """加载动作"""
        print("load action...")

    @pyqtSlot(str)
    def select_action(self, action_name: str):
        """用户选择动作"""
        print(f"select_action: {action_name}")