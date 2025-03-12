from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QGroupBox,
                             QSpinBox, QCheckBox, QTableWidget, QVBoxLayout)
from .base_page import BasePage
from app.core.config import StyleSheet


class ManualPage(BasePage):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化手动规划页面"""
        self.init_power_controls() # 电源控制区
        self.init_connector_controls() # 接头选择区
        self.init_sequence_controls() # 序列管理区
        self.init_action_controls() # 动作生成区
        self.init_part_table()  # 部位信息展示表格
        self.init_status() # 状态显示

    def init_power_controls(self):
        """电源控制组件"""
        hbox = QHBoxLayout()
        self.power_on_btn = QPushButton("上电")
        self.power_off_btn = QPushButton("断电")

        for btn in [self.power_on_btn, self.power_off_btn]:
            btn.setFixedSize(120, 40)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

    def init_connector_controls(self):
        """接头选择组件"""
        group = QGroupBox("接头：ID1")
        grid = QGridLayout()

        # 左半身关节
        left_joints = [
            ("摆头", 0, 0),
            ("左肩前摆", 1, 0),
            ("左肘", 2, 0),
            ("左髋前摆", 3, 0),
            ("左髋侧摆", 4, 0),
            ("左膝", 5, 0)
        ]

        # 右半身关节
        right_joints = [
            ("抬头", 0, 2),
            ("右肩前摆", 1, 2),
            ("右肘", 2, 2),
            ("右髋前摆", 3, 2),
            ("右髋侧摆", 4, 2),
            ("右膝", 5, 2)
        ]

        # 添加关节标签
        for name, row, col in left_joints + right_joints:
            label = QLabel(f"{name}:")
            grid.addWidget(label, row, col)

        # 添加角度输入框
        self.joint_inputs = {}
        for name, row, col in left_joints + right_joints:
            spinbox = QSpinBox()
            spinbox.setRange(-180, 180)
            spinbox.setSuffix("°")
            spinbox.setFixedWidth(100)
            self.joint_inputs[name] = spinbox
            grid.addWidget(spinbox, row, col + 1)

        group.setLayout(grid)
        self.layout.addWidget(group)

    def init_sequence_controls(self):
        """序列管理组件"""
        hbox = QHBoxLayout()
        self.add_seq_btn = QPushButton("加入序列")
        self.clear_seq_btn = QPushButton("清除序列")
        self.reset_btn = QPushButton("复位")

        for btn in [self.add_seq_btn, self.clear_seq_btn, self.reset_btn]:
            btn.setFixedSize(120, 40)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

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