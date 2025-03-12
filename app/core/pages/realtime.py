from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QComboBox, QPushButton, QGroupBox,
                             QFormLayout, QLineEdit, QLabel, QHBoxLayout, QSlider)
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
        self.load_btn = QPushButton("加载")
        self.load_btn.setFixedWidth(80)
        hbox.addWidget(QLabel("动作选择:"))
        hbox.addWidget(self.action_combo)
        hbox.addWidget(self.load_btn)
        self.layout.addLayout(hbox)

        # 参数设置
        self.init_parameters()
        self.init_execute_controls()
        self.init_notice()

    def init_parameters(self):
        group = QGroupBox("参数设置")
        form = QFormLayout()

        self.bpm_slider = QSlider(Qt.Horizontal)
        self.bpm_slider.setRange(10, 40)
        self.bpm_slider.setValue(22)
        self.bpm_label = QLabel("22 bpm")
        self.bpm_slider.valueChanged.connect(lambda: self.bpm_label.setText(f"{self.bpm_slider.value()} bpm"))

        self.amp_slider = QSlider(Qt.Horizontal)
        self.amp_slider.setRange(10, 50)
        self.amp_slider.setValue(20)
        self.amp_label = QLabel("20 mm")
        self.amp_slider.valueChanged.connect(lambda: self.amp_label.setText(f"{self.amp_slider.value()} mm"))

        self.hr_slider = QSlider(Qt.Horizontal)
        self.hr_slider.setRange(30, 100)
        self.hr_slider.setValue(50)
        self.hr_label = QLabel("50 bpm")
        self.hr_slider.valueChanged.connect(lambda: self.hr_label.setText(f"{self.hr_slider.value()} bpm"))

        bpm_layout = QHBoxLayout()
        bpm_layout.addWidget(self.bpm_slider)
        bpm_layout.addWidget(self.bpm_label)
        form.addRow("呼吸频率 (bpm):", bpm_layout)

        amp_layout = QHBoxLayout()
        amp_layout.addWidget(self.amp_slider)
        amp_layout.addWidget(self.amp_label)
        form.addRow("呼吸幅度 (mm):", amp_layout)

        hr_layout = QHBoxLayout()
        hr_layout.addWidget(self.hr_slider)
        hr_layout.addWidget(self.hr_label)
        form.addRow("心跳频率 (bpm):", hr_layout)

        group.setLayout(form)
        self.layout.addWidget(group)

    def init_execute_controls(self):
        hbox = QHBoxLayout()
        self.power_on_btn = QPushButton("上电")
        self.execute_btn = QPushButton("执行")
        self.stop_btn = QPushButton("停止")
        for btn in [self.power_on_btn, self.execute_btn, self.stop_btn]:
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