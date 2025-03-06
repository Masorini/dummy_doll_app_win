from app.core.controller.teachingController import TeachingController
from app.core.pages.teaching import TeachingPage
from app.core.connector.pageConnector import PageConnector

class TeachingPageConnector(PageConnector):
    def __init__(self, page: TeachingPage, controller: TeachingController):
        super().__init__(page, controller)
        self.init_connector()
        print("connected")
        pass

    def init_connector(self):        
        # 确保连接时忽略参数（如果方法不需要参数）
        self.page.power_on_btn.clicked.connect(lambda: self.controller.power_on())