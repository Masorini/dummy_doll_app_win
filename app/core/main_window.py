from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout, QToolButton, QLabel
from app.core.config import StyleSheet
from .connector.library_connector import LibraryConnector
from .connector.posture_connector import PostureConnector
from .connector.realtime_connector import RealtimeConnector
from .controller.library_controller import LibraryController
from .controller.posture_controller import PostureController
from .controller.realtime_controller import RealtimeController
from .pages.offline import OfflinePage
from .pages.realtime import RealtimePage
from .pages.teaching import TeachingPage
from .pages.manual import ManualPage
from .pages.posture import PosturePage
from .pages.library import LibraryPage
from .connector.teaching_page_connector import TeachingPageConnector
from .controller.teaching_controller import TeachingController


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CPD目标物控制器-sheree汽车")  # 设置窗口标题
        self.init_ui()

    def init_ui(self):
        """初始化UI布局"""
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 添加顶部标题栏
        self.init_title_bar(main_layout)
        # 添加导航栏
        self.init_navigation(main_layout)
        # 初始化页面堆栈
        self.init_pages(main_layout)
        # 初始化业务逻辑模块
        self.init_contorller()
        # 初始化连接器
        self.init_connector()

    def init_title_bar(self, main_layout):
        """初始化顶部标题栏"""
        title_layout = QHBoxLayout()

        # 主标题
        title_label = QLabel("智能座舱儿童遗留目标物")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        # 感叹号按钮 todo: 尺寸修改未生效
        self.info_btn = QToolButton()
        self.info_btn.setIcon(QIcon("app/resources/icons/warning2.png"))  # 需要提供图标资源
        self.info_btn.setToolTip("系统状态提示")
        self.info_btn.setStyleSheet(StyleSheet.QToolButton)

        title_layout.addWidget(title_label)
        title_layout.addStretch()  # 添加弹性空间
        title_layout.addWidget(self.info_btn)

        main_layout.addLayout(title_layout)

    def init_navigation(self, main_layout):
        """初始化横向导航栏"""
        nav_layout = QHBoxLayout()
        nav_layout.setSpacing(10)  # 设置按钮间距

        # 导航按钮
        self.nav_buttons = {}
        nav_items = ['离线控制', '实时调试', '示教规划', '手动规划', '座姿配置', '库管理']
        for item in nav_items:
            btn = QPushButton(item)
            btn.setCheckable(True)
            btn.setFixedSize(120, 40)
            btn.setStyleSheet(StyleSheet.NAV_BUTTON)
            btn.clicked.connect(lambda _, x=item: self.switch_page(x))
            self.nav_buttons[item] = btn
            nav_layout.addWidget(btn)

        main_layout.addLayout(nav_layout)

    def init_pages(self, main_layout):
        """初始化页面堆栈"""
        self.stacked_layout = QStackedLayout()
        main_layout.addLayout(self.stacked_layout)

        # 初始化页面
        self.pages = {
            '离线控制': OfflinePage(),
            '实时调试': RealtimePage(),
            '示教规划': TeachingPage(),
            '手动规划': ManualPage(),
            '座姿配置': PosturePage(),
            '库管理': LibraryPage()
        }

        for name, page in self.pages.items():
            self.stacked_layout.addWidget(page)

    def init_contorller(self):
        self.contorllers = {
            '离线控制': None,
            '实时调试': RealtimeController(),
            '示教规划': TeachingController(),
            '手动规划': None,
            '座姿配置': PostureController(),
            '库管理': LibraryController(),
        }

    def init_connector(self):
        self.conectors = {
            '离线控制': None,
            '实时调试': RealtimeConnector(self.pages['实时调试'], self.contorllers['实时调试']),
            '示教规划': TeachingPageConnector(self.pages['示教规划'], self.contorllers['示教规划']),
            '手动规划': None,
            '座姿配置': PostureConnector(self.pages['座姿配置'], self.contorllers['座姿配置']),
            '库管理': LibraryConnector(self.pages['库管理'], self.contorllers['库管理']),
        }

    def switch_page(self, page_name):
        """切换页面"""
        for btn in self.nav_buttons.values():
            btn.setChecked(False)
        self.nav_buttons[page_name].setChecked(True)
        self.stacked_layout.setCurrentWidget(self.pages[page_name])
