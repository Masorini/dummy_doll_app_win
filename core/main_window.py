from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout
from .pages.offline import OfflinePage
from .pages.realtime import RealtimePage
from core.config import StyleSheet, Dimensions


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化关键属性
        self.nav_buttons = {}
        self.pages = {}
        self.main_layout = QHBoxLayout(self)  # 主布局直接绑定到窗口

        # 调整初始化顺序
        self.setFixedSize(*Dimensions.MAIN_WINDOW)
        self.init_ui()  # 先初始化UI框架
        self.init_navigation()  # 再初始化导航
        self.init_pages()  # 最后初始化页面

    def init_ui(self):
        """统一初始化UI框架"""
        # 创建页面堆栈布局
        self.stacked_layout = QStackedLayout()  # 关键修复点
        right_widget = QWidget()
        right_widget.setLayout(self.stacked_layout)
        self.main_layout.addWidget(right_widget)

    def init_navigation(self):
        """初始化导航栏"""
        nav_widget = QWidget()
        nav_layout = QVBoxLayout()
        nav_widget.setLayout(nav_layout)
        nav_widget.setFixedWidth(150)

        nav_items = ['离线控制', '实时调试', '示教规划', '手动规划', '座姿配置', '库管理']
        for item in nav_items:
            btn = QPushButton(item)
            btn.setCheckable(True)
            btn.setFixedSize(*Dimensions.NAV_BUTTON)
            btn.setStyleSheet(StyleSheet.NAV_BUTTON)
            btn.clicked.connect(lambda _, x=item: self.switch_page(x))
            self.nav_buttons[item] = btn
            nav_layout.addWidget(btn)

        nav_layout.addStretch()
        self.main_layout.addWidget(nav_widget)

    def init_pages(self):
        """初始化所有页面"""
        # 创建页面实例
        self.pages['离线控制'] = OfflinePage()
        self.pages['实时调试'] = RealtimePage()

        # 将页面添加到堆栈布局
        for name, page in self.pages.items():
            self.stacked_layout.addWidget(page)  # 此时stacked_layout已存在

        # 默认显示第一个页面
        self.switch_page('离线控制')

    def switch_page(self, page_name):
        """执行页面切换"""
        for btn in self.nav_buttons.values():
            btn.setChecked(False)
        self.nav_buttons[page_name].setChecked(True)
        self.stacked_layout.setCurrentWidget(self.pages[page_name])