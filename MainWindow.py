# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
#                              QPushButton, QTableWidget, QTableWidgetItem, QGroupBox,
#                              QRadioButton)
#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('CPD目标物控制器-哈哈哈哈汽车')
#         main_layout = QVBoxLayout()
#
#         # 主标题
#         title = QLabel('CPD目标物控制器-哈哈哈哈汽车')
#         title.setStyleSheet('font-size: 20px; font-weight: bold;')
#         main_layout.addWidget(title)
#
#         # 子标题
#         subtitle = QLabel('智能座舱儿童遗留目标物')
#         subtitle.setStyleSheet('font-size: 16px; margin-bottom: 15px;')
#         main_layout.addWidget(subtitle)
#
#         # 功能按钮行
#         btn_names = ['离线控制', '实时调试', '示教规划', '手动规划', '座姿配置', '库管理']
#         btn_layout = QHBoxLayout()
#         for name in btn_names:
#             btn = QPushButton(name)
#             btn.setFixedHeight(35)
#             btn_layout.addWidget(btn)
#         main_layout.addLayout(btn_layout)
#
#         # 状态表格
#         table = QTableWidget()
#         table.setRowCount(4)
#         table.setColumnCount(6)
#         table.horizontalHeader().setVisible(False)
#         table.verticalHeader().setVisible(False)
#
#         # 填充表格数据
#         table_data = [
#             ['目标物状态', '', '', '', '', ''],
#             ['电池电压', '', '', '0V', '', ''],
#             ['电机温度', '', '', '未知', '', ''],
#             ['动作', '', '', '1', '', '']
#         ]
#         for row in range(4):
#             for col in range(6):
#                 item = QTableWidgetItem(table_data[row][col])
#                 table.setItem(row, col, item)
#         table.setFixedHeight(180)
#         main_layout.addWidget(table)
#
#         # 加载动作组
#         action_group = QGroupBox('加载动作')
#         action_layout = QVBoxLayout()
#         modes = ['仅呼吸', '呼吸动作', '仅呼吸心跳', '呼吸心跳加动作']
#         self.radios = [QRadioButton(mode) for mode in modes]
#         for radio in self.radios:
#             action_layout.addWidget(radio)
#         action_group.setLayout(action_layout)
#         main_layout.addWidget(action_group)
#
#         # 上电控制
#         power_layout = QHBoxLayout()
#         self.run_btn = QPushButton('运行')
#         self.stop_btn = QPushButton('停止')
#         self.run_btn.setFixedWidth(100)
#         self.stop_btn.setFixedWidth(100)
#         power_layout.addStretch()
#         power_layout.addWidget(self.run_btn)
#         power_layout.addWidget(self.stop_btn)
#         power_layout.addStretch()
#         main_layout.addLayout(power_layout)
#
#         # 服务器状态
#         server_layout = QHBoxLayout()
#         server_label = QLabel('连接服务器状态:')
#         self.status_label = QLabel('待机！')
#         self.status_label.setStyleSheet('color: #666666; font-style: italic;')
#         server_layout.addStretch()
#         server_layout.addWidget(server_label)
#         server_layout.addWidget(self.status_label)
#         server_layout.addStretch()
#         main_layout.addLayout(server_layout)
#
#         # 设置全局布局
#         main_layout.setSpacing(20)
#         main_layout.setContentsMargins(30, 20, 30, 30)
#         self.setLayout(main_layout)
#         self.setMinimumSize(800, 600)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     ex.show()
#     sys.exit(app.exec_())