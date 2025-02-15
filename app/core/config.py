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

    # 更新导航按钮样式
    NAV_BUTTON = """
           QPushButton {
               background: #F0F0F0;
               border: 1px solid #CCCCCC;
               padding: 8px;
               border-radius: 4px;
               font-size: 14px;
           }
           QPushButton:checked {
               background: #E0E0FF;
               border-color: #8888FF;
           }
           QPushButton:hover {
               background: #E0E0E0;
           }
       """

    QToolButton = """
            QToolButton{
                icon - size: 232px;
                border: none;
            }
        """

    class StyleSheet:
        # 新增部位选择样式
        PART_CHECKBOX = """
            QCheckBox {
                font-size: 14px;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
        """

        # 新增关节输入框样式
        JOINT_INPUT = """
            QSpinBox {
                font-size: 14px;
                padding: 5px;
            }
        """

        # 新增参数输入框样式
        POSTURE_INPUT = """
                QSpinBox {
                    font-size: 14px;
                    padding: 5px;
                }
            """

        # 新增文件标签样式
        FILE_LABEL = """
                QLabel {
                    color: #666666;
                    font-style: italic;
                    padding-left: 10px;
                }
            """


class Dimensions:
    """尺寸配置"""
    MAIN_WINDOW = (1000, 700)
    NAV_BUTTON = (140, 45)
    TABLE_ROW_HEIGHT = 40

    # 新增示教规划页专用配置
    TEACHING_BTN_SIZE = (140, 40)
    ACTION_INPUT_WIDTH = 200

    # 新增手动规划页专用配置
    JOINT_INPUT_WIDTH = 120
    SEQUENCE_BTN_SIZE = (120, 40)

    # 新增座姿配置页专用配置
    POSTURE_INPUT_WIDTH = 120
    ZERO_BTN_SIZE = (180, 45)

    # 新增库管理页专用配置
    UPLOAD_BTN_SIZE = (200, 40)
    ACTION_LIST_HEIGHT = 200
