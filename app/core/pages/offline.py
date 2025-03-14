from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import (QTableWidget, QTableWidgetItem, QGroupBox,
                             QRadioButton, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QComboBox)
from .base_page import BasePage
from app.core.config import StyleSheet


class StatusIndicator(QWidget):
    """目标物状态指示灯（绿色圆形）"""
    def __init__(self):
        super().__init__()
        self.setFixedSize(20, 20)

    def paintEvent(self, event):
        """绘制绿色圆形"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 180, 0))  # 绿色
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self.width(), self.height())

class OfflinePage(BasePage):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化 UI"""
        self.init_status_display()  # 目标物状态、电池电压、电机温度
        self.init_action_controls()  # 动作选择
        self.init_action_group()
        self.init_power_controls()  # 运行、停止
        self.init_server_status()  # 服务器状态

    def init_status_display(self):
        """目标物状态、电池电压、电机温度"""
        group = QGroupBox("状态信息")
        layout = QVBoxLayout()

        # 目标物状态
        hbox_status = QHBoxLayout()
        hbox_status.addWidget(QLabel("目标物状态:"))
        self.status_indicator = StatusIndicator()
        hbox_status.addWidget(self.status_indicator)
        hbox_status.addStretch()
        layout.addLayout(hbox_status)

        # 电池电压
        hbox_voltage = QHBoxLayout()
        hbox_voltage.addWidget(QLabel("电池电压:"))
        self.voltage_label = QLabel("12.5V")  # 固定展示
        hbox_voltage.addWidget(self.voltage_label)
        hbox_voltage.addStretch()
        layout.addLayout(hbox_voltage)

        # 电机温度
        hbox_temp = QHBoxLayout()
        hbox_temp.addWidget(QLabel("电机温度:"))
        self.temperature_label = QLabel("35°C")  # 固定展示
        hbox_temp.addWidget(self.temperature_label)
        hbox_temp.addStretch()
        layout.addLayout(hbox_temp)

        group.setLayout(layout)
        self.layout.addWidget(group)

    def init_action_controls(self):
        """动作选择"""
        group = QGroupBox("加载动作")
        layout = QHBoxLayout()

        self.action_select = QComboBox()
        self.action_select.addItems(["动作1", "动作2", "动作3"])  # 预设动作列表
        self.load_action_btn = QPushButton("加载数据")

        layout.addWidget(self.action_select)
        layout.addWidget(self.load_action_btn)
        group.setLayout(layout)
        self.layout.addWidget(group)

    def init_action_group(self):
        group = QGroupBox("加载动作")
        layout = QVBoxLayout()
        modes = ['仅呼吸', '呼吸动作', '仅呼吸心跳', '呼吸心跳加动作']
        self.radios = [QRadioButton(mode) for mode in modes]
        for radio in self.radios:
            layout.addWidget(radio)
        group.setLayout(layout)
        self.layout.addWidget(group)

    def init_power_controls(self):
        hbox = QHBoxLayout()
        self.power_on_btn = QPushButton("上电")
        self.run_btn = QPushButton("运行")
        self.stop_btn = QPushButton("停止")
        for btn in [self.power_on_btn, self.run_btn, self.stop_btn]:
            btn.setFixedSize(100, 40)
            hbox.addWidget(btn)
        self.layout.addLayout(hbox)

    def init_server_status(self):
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("连接服务器状态:"))
        self.status_label = QLabel("待机！")
        self.status_label.setStyleSheet(StyleSheet.WARNING_TEXT)
        hbox.addWidget(self.status_label)
        self.layout.addLayout(hbox)