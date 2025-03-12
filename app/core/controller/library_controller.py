from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from backend.services.servo_manager import ServoManager


class LibraryController(QObject):
    action_ids_loaded = pyqtSignal(list)  # 通知 UI 更新下拉框
    status_updated = pyqtSignal(str)  # 通知 UI 更新状态栏
    action_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.servo = ServoManager(1)  # TODO: 未来修改 ID
        self.available_action_ids = []  # 存储可选动作 ID
        self.selected_action_id = None

    def load_action_ids(self):
        """加载动作 ID 列表"""
        # TODO: 从实际数据源获取动作 ID
        print("load action ids...")

    @pyqtSlot(str)
    def upload_action_file(self):
        """上传动作文件"""
        print("upload_action_file...")

    @pyqtSlot()
    def save_to_flash(self):
        """保存到 Flash"""
        print("save tp flash...")
        # TODO: Flash 存储逻辑

    def select_action(self, action):
        print(f"Selected action: {action}")
        self.action_selected.emit(action)