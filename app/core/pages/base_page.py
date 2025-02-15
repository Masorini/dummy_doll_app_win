from PyQt5.QtWidgets import QWidget, QVBoxLayout

class BasePage(QWidget):
    """所有页面的基础类"""
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(30, 20, 30, 30)
        self.layout.setSpacing(20)

    def add_section_title(self, text):
        """添加区域标题"""
        # 实现细节...