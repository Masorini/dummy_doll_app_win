import sqlite3
from sqlite3 import Connection, Row
from config.config import DB_PATH

class DatabaseManager:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.conn: Connection = None
        self.connect()
        self.create_tables()

    def connect(self):
        """建立数据库连接，并设置 RowFactory 以便结果以字典形式访问"""
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def create_tables(self):
        """创建保存动作数据的表"""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS Actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_name TEXT NOT NULL,
            head_swivel INTEGER,            -- 摆头
            head_tilt INTEGER,              -- 抬头
            left_shoulder_forward INTEGER,  -- 左肩前摆
            left_shoulder_side INTEGER,     -- 左肩侧摆
            left_elbow INTEGER,             -- 左肘
            right_shoulder_forward INTEGER, -- 右肩前摆
            right_shoulder_side INTEGER,    -- 右肩侧摆
            right_elbow INTEGER,            -- 右肘
            left_hip_forward INTEGER,       -- 左髋前摆
            left_hip_side INTEGER,          -- 左髋侧摆
            left_knee INTEGER,              -- 左膝
            right_hip_forward INTEGER,      -- 右髋前摆
            right_hip_side INTEGER,         -- 右髋侧摆
            right_knee INTEGER,             -- 右膝
            is_zero INTEGER DEFAULT 0,      -- 是否零位（0: 否, 1: 是）
            is_valid INTEGER DEFAULT 1,     -- 状态标志（1: 有效, 0: 被删除或无效）
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor = self.conn.cursor()
        cursor.execute(create_table_sql)
        self.conn.commit()

    def insert_action(self, data: dict) -> int:
        """
        插入一条动作记录。
        data：字典形式，包含列名和对应的值（不包含 id、created_at、updated_at）
        返回值：新插入记录的 id
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        sql = f"INSERT INTO Actions ({columns}) VALUES ({placeholders})"
        cursor = self.conn.cursor()
        cursor.execute(sql, list(data.values()))
        self.conn.commit()
        return cursor.lastrowid

    def update_action(self, action_id: int, data: dict):
        """
        更新指定 id 的动作记录。
        """
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        sql = f"UPDATE Actions SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql, list(data.values()) + [action_id])
        self.conn.commit()

    def delete_action(self, action_id: int):
        """
        逻辑删除动作记录，将 is_valid 设为 0。
        """
        sql = "UPDATE Actions SET is_valid = 0, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (action_id,))
        self.conn.commit()

    def fetch_action(self, action_id: int) -> Row:
        """
        获取指定 id 的动作记录。
        """
        sql = "SELECT * FROM Actions WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (action_id,))
        return cursor.fetchone()

    def fetch_all_actions(self) -> list:
        """
        获取所有有效（未删除）的动作记录。
        """
        sql = "SELECT * FROM Actions WHERE is_valid = 1"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


# 可提供一个全局实例，方便其他模块直接导入使用
db_manager = DatabaseManager()
