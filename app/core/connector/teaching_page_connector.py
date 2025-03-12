from app.core.controller.teaching_controller import TeachingController
from app.core.pages.teaching import TeachingPage
from app.core.connector.page_connector import PageConnector

class TeachingPageConnector(PageConnector):
    def __init__(self, page: TeachingPage, controller: TeachingController):
        super().__init__(page, controller)
        self.init_connector()

    def init_connector(self):
        """连接 UI 组件和控制器"""
        self.page.power_on_btn.clicked.connect(lambda: self.controller.power_on())
        self.page.power_off_btn.clicked.connect(lambda: self.controller.power_off())
        self.page.enable_btn.clicked.connect(lambda: self.controller.enable_servo())
        self.page.disable_btn.clicked.connect(lambda: self.controller.disable_servo())

        self.page.read_pos_btn.clicked.connect(lambda: self.controller.read_pos())
        self.page.stop_read_btn.clicked.connect(lambda: self.controller.stop_read_pos())

        self.page.add_seq_btn.clicked.connect(lambda: self.controller.add_seq())
        self.page.clear_seq_btn.clicked.connect(lambda: self.controller.clear_seq())
        self.page.zero_seq_btn.clicked.connect(lambda: self.controller.zero_seq())

        self.page.generate_btn.clicked.connect(lambda: self.controller.generate())
