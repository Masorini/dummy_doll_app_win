import sys
from PyQt5.QtWidgets import QApplication
from app.core import init_resources
from app.core import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    init_resources()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())