from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QGroupBox,
                             QSpinBox, QCheckBox, QTableWidget, QVBoxLayout, QTableWidgetItem, QWidget)
from .base_page import BasePage
from app.core.config import StyleSheet


class ManualPage(BasePage):
    # 自定义信号，用于请求删除或插入序列行（参数为行索引）
    rowDeleteRequested = pyqtSignal(int)
    rowInsertRequested = pyqtSignal(int)

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
            btn.setFixedSize(120, 30)
            hbox.addWidget(btn)
        self.layout.addLayout(hbox)

    def init_connector_controls(self):
        """接头选择组件"""
        group = QGroupBox("各关节角度")
        grid = QGridLayout()

        # 左半身关节
        left_joints = [
            ("摆头", 0, 0),
            ("左肩前摆", 1, 0),
            ("左肩侧摆", 2, 0),
            ("左肘", 3, 0),
            ("左髋前摆", 4, 0),
            ("左髋侧摆", 5, 0),
            ("左膝", 6, 0)
        ]

        # 右半身关节
        right_joints = [
            ("抬头", 0, 2),
            ("右肩前摆", 1, 2),
            ("右肩侧摆", 2, 2),
            ("右肘", 3, 2),
            ("右髋前摆", 4, 2),
            ("右髋侧摆", 5, 2),
            ("右膝", 6, 2)
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
        self.reset_zero_btn = QPushButton("恢复零位")
        self.reset_flat_btn = QPushButton("恢复躺平位")

        for btn in [self.add_seq_btn, self.clear_seq_btn, self.reset_zero_btn, self.reset_flat_btn]:
            btn.setFixedSize(120, 30)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

    def init_action_controls(self):
        """动作生成组件"""
        hbox = QHBoxLayout()
        self.generate_btn = QPushButton("生成动作并保存")
        self.action_name_input = QLineEdit()
        self.action_name_input.setPlaceholderText("动作命名")

        self.generate_btn.setFixedSize(180, 30)
        self.action_name_input.setFixedHeight(30)

        hbox.addWidget(self.generate_btn)
        hbox.addWidget(self.action_name_input)
        self.layout.addLayout(hbox)

    def init_part_table(self):
        """部位信息展示表格"""
        group = QGroupBox("部位信息")
        vbox = QVBoxLayout()

        self.part_table = QTableWidget()
        self.part_table.setColumnCount(6)
        self.part_table.setHorizontalHeaderLabels(["头部", "左臂", "右臂", "左腿", "右腿", "操作"])
        self.part_table.setRowCount(0)
        self.part_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 设置表格不可编辑
        self.part_table.setMinimumHeight(150)

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

    def render_sequence_table(self, sequence_positions):
        """根据序列数据重绘表格"""
        self.part_table.setRowCount(0)
        for index, angles in enumerate(sequence_positions):
            # 根据要求格式化数据
            head = f"{angles.get('摆头', 0)}°, {angles.get('抬头', 0)}°"
            left_arm = f"{angles.get('左肩前摆', 0)}°, {angles.get('左肩侧摆', 0)}°, {angles.get('左肘', 0)}°"
            right_arm = f"{angles.get('右肩前摆', 0)}°, {angles.get('右肩侧摆', 0)}°, {angles.get('右肘', 0)}°"
            left_leg = f"{angles.get('左髋前摆', 0)}°, {angles.get('左髋侧摆', 0)}°, {angles.get('左膝', 0)}°"
            right_leg = f"{angles.get('右髋前摆', 0)}°, {angles.get('右髋侧摆', 0)}°, {angles.get('右膝', 0)}°"
            row_data = [head, left_arm, right_arm, left_leg, right_leg]
            self.part_table.insertRow(index)
            for col, data in enumerate(row_data):
                item = QTableWidgetItem(data)
                self.part_table.setItem(index, col, item)
            # 操作列：添加“删除”和“插入”按钮
            widget = QWidget()
            hbox = QHBoxLayout()
            btn_delete = QPushButton("删除")
            btn_insert = QPushButton("插入")
            btn_delete.setFixedSize(60, 30)
            btn_insert.setFixedSize(60, 30)
            hbox.addWidget(btn_delete)
            hbox.addWidget(btn_insert)
            hbox.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(hbox)
            self.part_table.setCellWidget(index, 5, widget)
            btn_delete.clicked.connect(lambda _, idx=index: self.rowDeleteRequested.emit(idx))
            btn_insert.clicked.connect(lambda _, idx=index: self.rowInsertRequested.emit(idx))

    def clear_sequence_table(self):
        """清空序列表格"""
        self.part_table.setRowCount(0)