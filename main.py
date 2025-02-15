import sys
from PyQt5.QtWidgets import QApplication
from core import init_resources
from core.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    init_resources()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())