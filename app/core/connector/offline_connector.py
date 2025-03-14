from app.core.controller.offline_controller import OfflineController
from app.core.pages.offline import OfflinePage
from app.core.connector.page_connector import PageConnector

class OfflineConnector(PageConnector):
    def __init__(self, page: OfflinePage, controller: OfflineController):
        super().__init__(page, controller)
        self.init_connector()

    def init_connector(self):
        """初始化信号连接"""
        self.page.power_on_btn.clicked.connect(self.controller.power_on)
        self.page.run_btn.clicked.connect(self.controller.run_action)
        self.page.stop_btn.clicked.connect(self.controller.stop_action)
        self.page.load_action_btn.clicked.connect(self.controller.load_action)
        self.page.action_select.currentTextChanged.connect(self.controller.select_action)

        # 绑定状态更新信号
        self.controller.status_updated.connect(self.page.status_label.setText)
