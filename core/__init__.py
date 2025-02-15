from PyQt5.QtGui import QIcon
import os

def init_resources():
    """初始化资源"""
    icon_path = os.path.join(os.path.dirname(__file__), "../resources/icons")
    QIcon.setThemeSearchPaths([icon_path])
    QIcon.setThemeName("default")