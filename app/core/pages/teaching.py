from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox, QGroupBox,
                             QLabel)
from .base_page import BasePage
from app.core.config import StyleSheet


class TeachingPage(BasePage):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化示教规划页面"""
        # 电源控制区
        self.init_power_controls()

        # 位置读取区
        self.init_position_controls()

        # 序列管理区
        self.init_sequence_controls()

        # 动作生成区
        self.init_action_controls()

        # 部位选择区
        self.init_part_selection()

        # 状态显示
        self.init_status()

    def init_power_controls(self):
        """电源控制组件"""
        hbox = QHBoxLayout()
        self.power_on_btn = QPushButton("上电")
        self.power_off_btn = QPushButton("断电")
        self.feces_btn = QPushButton("使能")
        self.feces_clear_btn = QPushButton("去使能")

        for btn in [self.power_on_btn, self.power_off_btn,
                    self.feces_btn, self.feces_clear_btn]:
            btn.setFixedSize(120, 40)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

    def init_position_controls(self):
        """位置读取组件"""
        hbox = QHBoxLayout()
        self.read_pos_btn = QPushButton("读取当前位置")
        self.stop_read_btn = QPushButton("停止读取")

        for btn in [self.read_pos_btn, self.stop_read_btn]:
            btn.setFixedSize(180, 45)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

    def init_sequence_controls(self):
        """序列管理组件"""
        group = QGroupBox("序列管理")
        grid = QGridLayout()

        self.add_seq_btn = QPushButton("加入序列")
        self.clear_seq_btn = QPushButton("清除序列")
        self.zero_seq_btn = QPushButton("零位加入序列")

        buttons = [
            (self.add_seq_btn, 0, 0),
            (self.clear_seq_btn, 0, 1),
            (self.zero_seq_btn, 0, 2)
        ]

        for btn, row, col in buttons:
            btn.setFixedSize(140, 40)
            grid.addWidget(btn, row, col)

        group.setLayout(grid)
        self.layout.addWidget(group)

    def init_action_controls(self):
        """动作生成组件"""
        hbox = QHBoxLayout()
        self.generate_btn = QPushButton("生成动作并保存")
        self.action_name_input = QLineEdit()
        self.action_name_input.setPlaceholderText("动作命名")

        self.generate_btn.setFixedSize(180, 45)
        self.action_name_input.setFixedHeight(40)

        hbox.addWidget(self.generate_btn)
        hbox.addWidget(self.action_name_input)
        self.layout.addLayout(hbox)

    def init_part_selection(self):
        """部位选择组件"""
        group = QGroupBox("部位选择")
        hbox = QHBoxLayout()

        self.parts = {
            "头部": QCheckBox("头部"),
            "左臂": QCheckBox("左臂"),
            "右臂": QCheckBox("右臂"),
            "左腿": QCheckBox("左腿"),
            "右腿": QCheckBox("右腿")
        }

        for part in self.parts.values():
            hbox.addWidget(part)

        group.setLayout(hbox)
        self.layout.addWidget(group)

    def init_status(self):
        """状态显示"""
        hbox = QHBoxLayout()
        self.status_label = QLabel("待机！")
        self.status_label.setStyleSheet(StyleSheet.WARNING_TEXT)
        hbox.addWidget(self.status_label)
        self.layout.addLayout(hbox)