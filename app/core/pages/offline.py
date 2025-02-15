from PyQt5.QtWidgets import (QTableWidget, QTableWidgetItem, QGroupBox,
                             QRadioButton, QPushButton, QLabel, QVBoxLayout, QHBoxLayout)
from .base_page import BasePage
from app.core.config import StyleSheet


class OfflinePage(BasePage):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 状态表格
        self.table = QTableWidget(4, 6)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setFixedHeight(180)

        # 填充数据
        table_data = [
            ['目标物状态', '', '', '', '', ''],
            ['电池电压', '', '', '0V', '', ''],
            ['电机温度', '', '', '未知', '', ''],
            ['动作', '', '', '1', '', '']
        ]
        for row, items in enumerate(table_data):
            for col, text in enumerate(items):
                self.table.setItem(row, col, QTableWidgetItem(text))
        self.layout.addWidget(self.table)

        # 加载动作组
        self.init_action_group()
        self.init_power_controls()
        self.init_server_status()

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
        self.run_btn = QPushButton("运行")
        self.stop_btn = QPushButton("停止")
        for btn in [self.run_btn, self.stop_btn]:
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