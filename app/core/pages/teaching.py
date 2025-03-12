from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox, QGroupBox,
                             QLabel, QTableWidget, QVBoxLayout, QTableWidgetItem)
from .base_page import BasePage
from app.core.config import StyleSheet


class TeachingPage(BasePage):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化示教规划页面"""
        self.init_power_controls()      # 电源控制区
        self.init_position_controls()   # 位置读取区
        self.init_sequence_controls()   # 序列管理区
        self.init_action_controls()     # 动作生成区
        self.init_part_table()          # 部位信息展示表格
        self.init_status()              # 状态显示

    def init_power_controls(self):
        """电源控制组件"""
        hbox = QHBoxLayout()
        self.power_on_btn = QPushButton("上电")
        self.power_off_btn = QPushButton("断电")
        self.enable_btn = QPushButton("使能")
        self.disable_btn = QPushButton("去使能")

        for btn in [self.power_on_btn, self.power_off_btn,
                    self.enable_btn, self.disable_btn]:
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

        for btn, pos in zip([self.add_seq_btn, self.clear_seq_btn, self.zero_seq_btn], [(0, 0), (0, 1), (0, 2)]):
            btn.setFixedSize(140, 40)
            grid.addWidget(btn, *pos)

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

    def init_part_table(self):
        """部位信息展示表格"""
        group = QGroupBox("部位信息")
        vbox = QVBoxLayout()

        self.part_table = QTableWidget()
        self.part_table.setColumnCount(5)
        self.part_table.setHorizontalHeaderLabels(["头部", "左臂", "右臂", "左腿", "右腿"])
        self.part_table.setRowCount(1)
        self.part_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 设置表格不可编辑

        vbox.addWidget(self.part_table)
        group.setLayout(vbox)
        self.layout.addWidget(group)

    def init_status(self):
        """状态显示"""
        hbox = QHBoxLayout()
        self.status_label = QLabel("待机！")
        self.status_label.setStyleSheet(StyleSheet.WARNING_TEXT)
        hbox.addWidget(self.status_label)
        self.layout.addLayout(hbox)

    def update_part_table(self, data):
        """更新表格内容"""
        for col, value in enumerate(data):
            self.part_table.setItem(0, col, QTableWidgetItem(str(value)))