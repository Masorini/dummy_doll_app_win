class StyleSheet:
    """样式表配置"""
    PAGE_TITLE = """
        QLabel {
            font-size: 16px;
            color: #333333;
            padding-bottom: 10px;
        }
    """

    WARNING_TEXT = """
        QLabel {
            color: #FF4444;
            font-size: 12px;
            font-style: italic;
        }
    """

    NAV_BUTTON = """
        QPushButton {
            background: #F0F0F0;
            border: 1px solid #CCCCCC;
            padding: 8px;
            border-radius: 4px;
        }
        QPushButton:checked {
            background: #E0E0FF;
            border-color: #8888FF;
        }
    """


class Dimensions:
    """尺寸配置"""
    MAIN_WINDOW = (1000, 700)
    NAV_BUTTON = (140, 45)
    TABLE_ROW_HEIGHT = 40