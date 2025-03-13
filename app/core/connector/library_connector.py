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

        self.page.action_id_select.currentTextChanged.connect(self.controller.select_action)


