from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QPushButton, QSpinBox, QLabel, QGroupBox)
from .base_page import BasePage
from app.core.config import StyleSheet


class PosturePage(BasePage):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化座姿配置页面"""
        # 电源控制区
        self.init_power_controls()

        # 座姿读取区
        self.init_posture_controls()

        # 手动配置区
        self.init_manual_config()

        # 零位管理区
        self.init_zero_position()

        # 状态显示
        self.init_status()

    def init_power_controls(self):
        """电源控制组件"""
        hbox = QHBoxLayout()
        self.power_on_btn = QPushButton("上电")
        self.enable_btn = QPushButton("使能")
        self.power_off_btn = QPushButton("断电")

        for btn in [self.power_on_btn, self.enable_btn, self.power_off_btn]:
            btn.setFixedSize(120, 40)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

    def init_posture_controls(self):
        """座姿读取组件"""
        hbox = QHBoxLayout()
        self.read_posture_btn = QPushButton("读取座姿")
        self.manual_config_btn = QPushButton("手动配置")

        for btn in [self.read_posture_btn, self.manual_config_btn]:
            btn.setFixedSize(180, 45)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

    def init_manual_config(self):
        """手动配置组件"""
        group = QGroupBox("手动配置")
        grid = QGridLayout()

        # 配置参数
        self.posture_inputs = {}
        for i in range(1, 15):
            label = QLabel(f"参数 {i}:")
            spinbox = QSpinBox()
            spinbox.setRange(0, 360)
            spinbox.setValue(60)  # 默认值
            spinbox.setFixedWidth(100)

            row = (i - 1) // 2
            col = (i - 1) % 2 * 2
            grid.addWidget(label, row, col)
            grid.addWidget(spinbox, row, col + 1)

            self.posture_inputs[i] = spinbox

        group.setLayout(grid)
        self.layout.addWidget(group)

    def init_zero_position(self):
        """零位管理组件"""
        hbox = QHBoxLayout()
        self.set_zero_btn = QPushButton("设置当前坐姿为零位")
        self.test_zero_btn = QPushButton("测试：运行至零位")
        self.save_flash_btn = QPushButton("保存至Flash")

        for btn in [self.set_zero_btn, self.test_zero_btn, self.save_flash_btn]:
            btn.setFixedSize(180, 45)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

    def init_status(self):
        """状态显示"""
        hbox = QHBoxLayout()
        self.status_label = QLabel("待机！")
        self.status_label.setStyleSheet(StyleSheet.WARNING_TEXT)
        hbox.addWidget(self.status_label)
        self.layout.addLayout(hbox)