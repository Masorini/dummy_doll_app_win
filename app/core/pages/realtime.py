from PyQt5.QtWidgets import (QComboBox, QPushButton, QGroupBox,
                             QFormLayout, QLineEdit, QLabel, QHBoxLayout)
from .base_page import BasePage
from app.core.config import StyleSheet


class RealtimePage(BasePage):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 动作选择
        hbox = QHBoxLayout()
        self.action_combo = QComboBox()
        self.action_combo.addItems(["动作库1", "动作库2", "动作库3"])
        load_btn = QPushButton("加载")
        load_btn.setFixedWidth(80)
        hbox.addWidget(QLabel("动作选择:"))
        hbox.addWidget(self.action_combo)
        hbox.addWidget(load_btn)
        self.layout.addLayout(hbox)

        # 参数设置
        self.init_parameters()
        self.init_execute_controls()
        self.init_notice()

    def init_parameters(self):
        group = QGroupBox("参数设置")
        form = QFormLayout()

        self.bpm_input = QLineEdit("22")
        self.amp_input = QLineEdit("20")
        self.hr_input = QLineEdit("50")

        form.addRow("呼吸频率 (bpm):", self.bpm_input)
        form.addRow("呼吸幅度 (mm):", self.amp_input)
        form.addRow("心跳频率 (bpm):", self.hr_input)

        group.setLayout(form)
        self.layout.addWidget(group)

    def init_execute_controls(self):
        hbox = QHBoxLayout()
        self.execute_btn = QPushButton("执行")
        self.stop_btn = QPushButton("停止")
        for btn in [self.execute_btn, self.stop_btn]:
            btn.setFixedSize(120, 45)
            hbox.addWidget(btn)
        self.layout.addLayout(hbox)

    def init_notice(self):
        notice = QLabel(
            "注意：实时调试需保持手机或平板处于活动状态，并维持在该页面。"
            "调试完成后的动作数据需上传至目标物，进行离线操作。"
        )
        notice.setWordWrap(True)
        notice.setStyleSheet(StyleSheet.WARNING_TEXT)
        self.layout.addWidget(notice)