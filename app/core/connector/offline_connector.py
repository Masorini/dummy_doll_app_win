from app.core.controller.offline_controller import OfflineController
from app.core.pages.offline import OfflinePage
from app.core.connector.page_connector import PageConnector

class OfflinePageConnector(PageConnector):
    def __init__(self,page: OfflinePage,controller: OfflineController):
        super().__init__(page,controller)
        self.init_connector()
        pass

    def init_connector(self):

        self.page.run_btn.clicked.connect(lambda:self.controller.run())