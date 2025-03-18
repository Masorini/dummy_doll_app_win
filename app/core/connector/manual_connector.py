from app.core.controller.manual_controller import ManualController
from app.core.pages.manual import ManualPage
from app.core.connector.page_connector import PageConnector

class ManualConnector(PageConnector):
    def __init__(self, page: ManualPage, controller: ManualController):
        super().__init__(page, controller)
        self.init_connector()

    def init_connector(self):
        """初始化信号连接"""
        # 绑定电源、序列管理、复位、生成动作按钮
        self.page.power_on_btn.clicked.connect(self.controller.power_on)
        self.page.power_off_btn.clicked.connect(self.controller.power_off)
        self.page.add_seq_btn.clicked.connect(self.controller.add_to_sequence)
        self.page.clear_seq_btn.clicked.connect(self.controller.clear_sequence)
        self.page.reset_zero_btn.clicked.connect(self.controller.reset_to_zero)
        self.page.reset_flat_btn.clicked.connect(self.controller.reset_to_flat)
        self.page.generate_btn.clicked.connect(self.controller.generate_action)

        # 绑定状态更新信号
        self.controller.status_updated.connect(self.page.status_label.setText)

        # 绑定关节角度输入框的变化事件
        for joint_name, spinbox in self.page.joint_inputs.items():
            spinbox.valueChanged.connect(lambda value, name=joint_name: self.controller.update_joint_angle(name, value))

        # 绑定序列表格中行操作信号
        self.page.rowDeleteRequested.connect(self.controller.delete_sequence_row)
        self.page.rowInsertRequested.connect(self.controller.insert_sequence_row)