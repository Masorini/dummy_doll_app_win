from PyQt5.QtWidgets import QFileDialog

from app.core.controller.library_controller import LibraryController
from app.core.pages.library import LibraryPage
from app.core.connector.page_connector import PageConnector

class LibraryConnector(PageConnector):
    def __init__(self, page: LibraryPage, controller: LibraryController):
        super().__init__(page, controller)
        self.init_connector()

    def init_connector(self):
        """初始化信号连接"""
        # 绑定按钮事件
        self.page.upload_file_btn.clicked.connect(lambda: self.controller.upload_action_file())
        self.page.refresh_btn.clicked.connect(lambda: self.controller.load_action_ids())
        self.page.save_flash_btn.clicked.connect(lambda: self.controller.save_to_flash())

        # 监听 controller 信号，更新 UI
        # self.controller.action_ids_loaded.connect(self.update_action_id_list)
        # self.controller.status_updated.connect(self.update_status_label)

        self.page.action_id_select.currentTextChanged.connect(self.controller.select_action)

        # 初始化时加载动作 ID
        # self.controller.load_action_ids()

    def handle_upload_action_file(self):
        """用户点击上传文件按钮"""
        file_path, _ = QFileDialog.getOpenFileName(
            self.page, "选择动作文件", "", "动作文件 (*.act)"
        )
        if file_path:
            self.page.file_label.setText(file_path)
            self.controller.upload_action_file(file_path)  # 直接传入文件路径

    def update_action_id_list(self, action_ids):
        """更新下拉框的动作 ID 列表"""
        print("update_action_id_list...")
        self.page.action_id_select.clear()
        self.page.action_id_select.addItems(action_ids)

    def update_status_label(self, message):
        """更新状态栏文本"""
        print("update_status_label...")
        self.page.status_label.setText(message)
