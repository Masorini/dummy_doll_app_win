from app.core.controller.posture_controller import PostureController
from app.core.pages.posture import PosturePage
from app.core.connector.page_connector import PageConnector

class PostureConnector(PageConnector):
    def __init__(self, page: PosturePage, controller: PostureController):
        super().__init__(page, controller)
        self.init_connector()

    def init_connector(self):
        """Initialize all signal-slot connections."""
        # Connecting power control buttons
        self.page.power_on_btn.clicked.connect(lambda: self.controller.power_on())
        self.page.power_off_btn.clicked.connect(lambda: self.controller.power_off())
        self.page.enable_btn.clicked.connect(lambda: self.controller.enable())
        # self.page.disable_btn.clicked.connect(lambda: self.controller.disable())

        # Connecting posture control buttons
        self.page.read_posture_btn.clicked.connect(lambda: self.controller.read_posture())
        self.page.manual_config_btn.clicked.connect(lambda: self.controller.apply_manual_config())

        # Connecting zero-position buttons
        self.page.set_zero_btn.clicked.connect(lambda: self.controller.set_zero_position())
        self.page.test_zero_btn.clicked.connect(lambda: self.controller.test_zero_position())
        self.page.save_flash_btn.clicked.connect(lambda: self.controller.save_to_flash())

        # 绑定手动配置区的 QSpinBox 变化信号
        for param_index, spinbox in self.page.posture_inputs.items():
            spinbox.valueChanged.connect(lambda value, i=param_index: self.controller.update_posture_param(i, value))
