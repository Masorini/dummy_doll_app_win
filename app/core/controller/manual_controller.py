from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from backend.services.db_manager import db_manager
from backend.services.servo_manager import ServoManager


class ManualController(QObject):
    status_updated = pyqtSignal(str)

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.servo = ServoManager(1)  # TODO: 未来修改 ID
        self.joint_angles = {}
        self.sequence_positions = []  # 保存每次加入序列时的原始角度数据字典
        # 定义零位配置（可根据实际需求调整）
        self.zero_config = {
            "摆头": 30,
            "抬头": 30,
            "左肩前摆": 40,
            "左肩侧摆": 50,
            "左肘": 60,
            "右肩前摆": 40,
            "右肩侧摆": 50,
            "右肘": 60,
            "左髋前摆": 20,
            "左髋侧摆": 20,
            "左膝": 30,
            "右髋前摆": 20,
            "右髋侧摆": 20,
            "右膝": 30,
        }
        # 可设置一个标志判断是否为零位（这里仅作为示例，实际逻辑请按需求实现）
        self.is_zero_condition = False

    @pyqtSlot()
    def power_on(self):
        """上电"""
        print("power on...")

    @pyqtSlot()
    def power_off(self):
        """断电"""
        print("power off...")

    @pyqtSlot()
    def add_to_sequence(self):
        """加入当前关节角度到序列"""
        print("add to sequence...")
        angles = {joint: spinbox.value() for joint, spinbox in self.page.joint_inputs.items()}
        self.sequence_positions.append(angles)
        self.page.render_sequence_table(self.sequence_positions)
        print("加入序列：", angles)

    @pyqtSlot()
    def clear_sequence(self):
        """清空序列"""
        print("clear sequence...")
        reply = QMessageBox.question(self.page, '确认', '确定要清除所有序列数据吗?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.sequence_positions = []
            self.page.clear_sequence_table()
            print("序列已清空。")

    @pyqtSlot(int)
    def delete_sequence_row(self, index):
        """删除指定序列行"""
        if 0 <= index < len(self.sequence_positions):
            removed = self.sequence_positions.pop(index)
            self.page.render_sequence_table(self.sequence_positions)
            print(f"删除第 {index} 行：", removed)

    @pyqtSlot(int)
    def insert_sequence_row(self, index):
        """在指定行下方插入一行当前关节角度数据"""
        angles = {joint: spinbox.value() for joint, spinbox in self.page.joint_inputs.items()}
        self.sequence_positions.insert(index + 1, angles)
        self.page.render_sequence_table(self.sequence_positions)
        print(f"在第 {index} 行下方插入：", angles)

    @pyqtSlot()
    def reset_to_zero(self):
        """复位所有关节"""
        print("reset to zero...")
        for joint, spinbox in self.page.joint_inputs.items():
            spinbox.setValue(self.zero_config.get(joint, 0))
        print("恢复到零位配置。")

    @pyqtSlot()
    def reset_to_flat(self):
        """恢复躺平位（所有角度均为 0）"""
        print("reset to flat...")
        for spinbox in self.page.joint_inputs.values():
            spinbox.setValue(0)
        print("恢复到躺平位。")

    @pyqtSlot(str, int)
    def update_joint_angle(self, joint_name, angle):
        """更新关节角度并打印日志"""
        self.joint_angles[joint_name] = angle
        print(f"关节: {joint_name}, 角度: {angle}°")

    @pyqtSlot()
    def generate_action(self):
        """生成动作并保存到数据库（动作由多个序列位置组成）"""
        action_name = self.page.action_name_input.text().strip()
        if not action_name:
            self.status_updated.emit("请先输入动作名称！")
            return
        if not self.sequence_positions:
            self.status_updated.emit("序列为空，请先加入序列！")
            return
        try:
            # 插入总体动作记录（新创建的 Actions 表）
            action_id = db_manager.insert_action(action_name)
            # 将每个序列位置记录插入到 ActionPositions 表中
            db_manager.insert_action_positions(action_id, self.sequence_positions)
            self.status_updated.emit(f"动作 '{action_name}' 保存成功，ID: {action_id}")
            print(f"Saved action {action_name} with ID: {action_id}")
        except Exception as e:
            self.status_updated.emit("保存动作失败！")
            print(f"Error saving action: {e}")

    # @pyqtSlot()
    # def generate_action(self):
    #     """生成动作并保存到数据库"""
    #     print("generate action...")
    #     action_name = self.page.action_name_input.text().strip()
    #     print(f"action_name: {action_name}")
    #     if not action_name:
    #         self.status_updated.emit("请先输入动作名称！")
    #         return
    #
    #     # 构建动作数据字典，注意键名需与数据库表中字段对应
    #     data = {
    #         "action_name": action_name,
    #         "head_swivel": self.joint_angles.get("摆头", 0),
    #         "head_tilt": self.joint_angles.get("抬头", 0),
    #         "left_shoulder_forward": self.joint_angles.get("左肩前摆", 0),
    #         "left_shoulder_side": self.joint_angles.get("左肩侧摆", 0),
    #         "left_elbow": self.joint_angles.get("左肘", 0),
    #         "right_shoulder_forward": self.joint_angles.get("右肩前摆", 0),
    #         "right_shoulder_side": self.joint_angles.get("右肩侧摆", 0),
    #         "right_elbow": self.joint_angles.get("右肘", 0),
    #         "left_hip_forward": self.joint_angles.get("左髋前摆", 0),
    #         "left_hip_side": self.joint_angles.get("左髋侧摆", 0),
    #         "left_knee": self.joint_angles.get("左膝", 0),
    #         "right_hip_forward": self.joint_angles.get("右髋前摆", 0),
    #         "right_hip_side": self.joint_angles.get("右髋侧摆", 0),
    #         "right_knee": self.joint_angles.get("右膝", 0),
    #         "is_zero": 1 if self.is_zero_condition else 0,
    #         "is_valid": 1
    #     }
    #
    #     try:
    #         action_id = db_manager.insert_action(data)
    #         print(f"action_id: {action_id}")
    #         self.status_updated.emit(f"动作 '{action_name}' 保存成功，ID: {action_id}")
    #         print(f"Saved action {action_name} with ID: {action_id}")
    #     except Exception as e:
    #         self.status_updated.emit("保存动作失败！")
    #         print(f"Error saving action: {e}")



