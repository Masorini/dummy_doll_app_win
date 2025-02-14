# 智能座舱儿童遗留目标物控制系统

## 项目结构说明

### 目录结构树
├── MainWindow.py # 遗留主窗口文件（建议迁移至core目录）
├── core/ # 核心功能模块
│ ├── init.py # Python包标识文件
│ ├── config.py # 样式/尺寸配置中心
│ ├── main_window.py # 主窗口实现（核心入口）
│ ├── pages/ # 功能页面模块
│ │ ├── init.py
│ │ ├── base_page.py # 页面基类（通用布局/方法）
│ │ ├── offline.py # 离线控制页
│ │ └── realtime.py # 实时调试页
│ └── widgets/ # 自定义组件库
│ └── param_input.py # 参数输入组件
├── main.py # 程序启动入口
└── resources/ # 资源文件目录

### Directory Tree
├── MainWindow.py # Legacy main window file (recommended to migrate to core/)
├── core/ # Core functional modules
│ ├── init.py # Python package identifier
│ ├── config.py # Style/dimension configuration center
│ ├── main_window.py # Main window implementation (core entry)
│ ├── pages/ # Functional page modules
│ │ ├── init.py
│ │ ├── base_page.py # Page base class (common layouts/methods)
│ │ ├── offline.py # Offline control page
│ │ └── realtime.py # Real-time debugging page
│ └── widgets/ # Custom component library
│ └── param_input.py # Parameter input widget
├── main.py # Program entry point
└── resources/ # Resource directory

### 文件职责说明

| 文件/目录                | 功能说明                                                                 |
|--------------------------|------------------------------------------------------------------------|
| `main.py`                | 应用启动入口，初始化QApplication和主窗口                                |
| `core/main_window.py`     | 主窗口类实现，包含：<br>• 导航栏管理<br>• 页面堆栈布局<br>• 全局状态控制 |
| `core/config.py`          | 中央配置管理：<br>• 界面样式表(StyleSheet)<br>• 组件尺寸(Dimensions)     |
| `core/pages/base_page.py` | 页面基类，提供：<br>• 统一布局规范<br>• 通用组件添加方法                 |
| `core/pages/offline.py`   | 离线控制页功能：<br>• 状态监控表格<br>• 动作加载控制<br>• 电源管理       |
| `core/pages/realtime.py`  | 实时调试页功能：<br>• 参数输入验证<br>• 动作执行控制<br>• 数据通信管理   |
| `core/widgets/`           | 自定义控件库：<br>• 参数输入框<br>• 状态指示灯<br>• 工业风格按钮         |
| `resources/`              | 资源文件存储：<br>• 图标资源(.ico/.png)<br>• 本地化文件<br>• 文档模板   |

## 运行说明

### 环境要求
```bash
Python 3.8+ 
PyQt5 == 5.15.4