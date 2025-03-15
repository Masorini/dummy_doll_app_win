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
        """创建动作相关的表"""
        # 总体动作表
        create_actions_table_sql = """
        CREATE TABLE IF NOT EXISTS Actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_name TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        # 动作序列位置表
        create_positions_table_sql = """
        CREATE TABLE IF NOT EXISTS ActionPositions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_id INTEGER,
            sequence_order INTEGER,
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
            is_zero INTEGER DEFAULT 0,
            is_valid INTEGER DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(action_id) REFERENCES Actions(id)
        );
        """
        cursor = self.conn.cursor()
        cursor.execute(create_actions_table_sql)
        cursor.execute(create_positions_table_sql)
        self.conn.commit()

    def insert_action(self, action_name: str) -> int:
        """
        插入一条总体动作记录，返回新记录的 id
        """
        sql = "INSERT INTO Actions (action_name) VALUES (?)"
        cursor = self.conn.cursor()
        cursor.execute(sql, (action_name,))
        self.conn.commit()
        return cursor.lastrowid

    def insert_action_positions(self, action_id: int, positions: list):
        """
        批量插入动作序列位置数据
        positions: list of dict，每个 dict 包含14个角度及 is_zero 标志
        """
        sql = """INSERT INTO ActionPositions 
                 (action_id, sequence_order, head_swivel, head_tilt, 
                  left_shoulder_forward, left_shoulder_side, left_elbow, 
                  right_shoulder_forward, right_shoulder_side, right_elbow, 
                  left_hip_forward, left_hip_side, left_knee, 
                  right_hip_forward, right_hip_side, right_knee, is_zero, is_valid)
                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        cursor = self.conn.cursor()
        for order, pos in enumerate(positions):
            cursor.execute(sql, (
                action_id,
                order,
                pos.get("摆头", 0),
                pos.get("抬头", 0),
                pos.get("左肩前摆", 0),
                pos.get("左肩侧摆", 0),
                pos.get("左肘", 0),
                pos.get("右肩前摆", 0),
                pos.get("右肩侧摆", 0),
                pos.get("右肘", 0),
                pos.get("左髋前摆", 0),
                pos.get("左髋侧摆", 0),
                pos.get("左膝", 0),
                pos.get("右髋前摆", 0),
                pos.get("右髋侧摆", 0),
                pos.get("右膝", 0),
                1 if pos.get("is_zero", False) else 0,
                1
            ))
        self.conn.commit()

    def update_action(self, action_id: int, data: dict):
        """
        更新指定 id 的动作记录
        """
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        sql = f"UPDATE Actions SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql, list(data.values()) + [action_id])
        self.conn.commit()

    def delete_action(self, action_id: int):
        """
        逻辑删除动作记录，将 is_valid 设为 0
        """
        sql = "UPDATE Actions SET is_valid = 0, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (action_id,))
        self.conn.commit()

    def fetch_action(self, action_id: int) -> Row:
        """
        获取指定 id 的动作记录
        """
        sql = "SELECT * FROM Actions WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (action_id,))
        return cursor.fetchone()

    def fetch_all_actions(self) -> list:
        """
        获取所有有效（未删除）的动作记录
        """
        sql = "SELECT * FROM Actions WHERE is_valid = 1"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


# 可提供一个全局实例，方便其他模块直接导入使用
db_manager = DatabaseManager()
