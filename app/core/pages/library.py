from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QPushButton,
                             QLabel, QListWidget, QFileDialog, QGroupBox, QLineEdit)
from .base_page import BasePage
from app.core.config import StyleSheet


class LibraryPage(BasePage):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化库管理页面"""
        # 动作库操作区
        self.init_library_controls()

        # 文件上传区
        self.init_upload_controls()

        # 状态显示
        self.init_status()

    def init_library_controls(self):
        """动作库操作组件"""
        hbox = QHBoxLayout()
        self.refresh_btn = QPushButton("刷新运动步态")
        self.save_flash_btn = QPushButton("保存至Flash")

        for btn in [self.refresh_btn, self.save_flash_btn]:
            btn.setFixedSize(180, 45)
            hbox.addWidget(btn)

        self.layout.addLayout(hbox)

    def init_upload_controls(self):
        """文件上传组件"""
        group = QGroupBox("动作文件管理")
        vbox = QVBoxLayout()

        # 动作ID输入
        hbox_id = QHBoxLayout()
        self.upload_id_btn = QPushButton("上传动作ID")
        self.action_id_input = QLineEdit()
        self.action_id_input.setPlaceholderText("输入动作ID")

        self.upload_id_btn.setFixedSize(120, 40)
        self.action_id_input.setFixedHeight(40)

        hbox_id.addWidget(self.upload_id_btn)
        hbox_id.addWidget(self.action_id_input)

        # 文件选择
        hbox_file = QHBoxLayout()
        self.upload_file_btn = QPushButton("上传选择的动作文件")
        self.file_label = QLabel("未选择文件")

        self.upload_file_btn.setFixedSize(200, 40)
        self.file_label.setStyleSheet(StyleSheet.WARNING_TEXT)

        hbox_file.addWidget(self.upload_file_btn)
        hbox_file.addWidget(self.file_label)

        # 动作列表
        self.action_list = QListWidget()
        self.action_list.setFixedHeight(200)

        vbox.addLayout(hbox_id)
        vbox.addLayout(hbox_file)
        vbox.addWidget(self.action_list)
        group.setLayout(vbox)
        self.layout.addWidget(group)

    def init_status(self):
        """状态显示"""
        hbox = QHBoxLayout()
        self.status_label = QLabel("待机！")
        self.status_label.setStyleSheet(StyleSheet.WARNING_TEXT)
        hbox.addWidget(self.status_label)
        self.layout.addLayout(hbox)

    def connect_signals(self):
        """连接信号槽"""
        self.upload_file_btn.clicked.connect(self.select_action_file)
        self.refresh_btn.clicked.connect(self.refresh_gait)
        self.save_flash_btn.clicked.connect(self.save_to_flash)

    def select_action_file(self):
        """选择动作文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择动作文件", "", "动作文件 (*.act)")
        if file_path:
            self.file_label.setText(file_path)
            # 处理文件上传逻辑...

    def refresh_gait(self):
        """刷新运动步态"""
        self.status_label.setText("正在刷新运动步态...")
        # 刷新逻辑...

    def save_to_flash(self):
        """保存到Flash"""
        self.status_label.setText("正在保存到Flash...")
        # Flash保存逻辑...