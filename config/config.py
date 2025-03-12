import os

# 获取项目根目录（假设 config 目录在项目根目录下）
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 数据库文件存放路径，建议在项目根目录下创建一个专门存放数据的文件夹，比如 data
DB_PATH = os.path.join(PROJECT_ROOT, 'app_data.db')
