from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from backend.services.db_manager import db_manager
from backend.services.servo_manager import ServoManager


class ManualController(QObject):
    status_updated = pyqtSignal(str)

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.servo = ServoManager(1)  # TODO: 未来修改 ID
        self.joint_angles = {}
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

    @pyqtSlot()
    def clear_sequence(self):
        """清空序列"""
        print("clear sequence...")

    @pyqtSlot()
    def reset_joints(self):
        """复位所有关节"""
        print("reset joints...")

    @pyqtSlot(str, int)
    def update_joint_angle(self, joint_name, angle):
        """更新关节角度并打印日志"""
        self.joint_angles[joint_name] = angle
        print(f"关节: {joint_name}, 角度: {angle}°")

    @pyqtSlot()
    def generate_action(self):
        """生成动作并保存到数据库"""
        print("generate action...")
        action_name = self.page.action_name_input.text().strip()
        print(f"action_name: {action_name}")
        if not action_name:
            self.status_updated.emit("请先输入动作名称！")
            return

        # 构建动作数据字典，注意键名需与数据库表中字段对应
        data = {
            "action_name": action_name,
            "head_swivel": self.joint_angles.get("摆头", 0),
            "head_tilt": self.joint_angles.get("抬头", 0),
            "left_shoulder_forward": self.joint_angles.get("左肩前摆", 0),
            "left_shoulder_side": self.joint_angles.get("左肩侧摆", 0),
            "left_elbow": self.joint_angles.get("左肘", 0),
            "right_shoulder_forward": self.joint_angles.get("右肩前摆", 0),
            "right_shoulder_side": self.joint_angles.get("右肩侧摆", 0),
            "right_elbow": self.joint_angles.get("右肘", 0),
            "left_hip_forward": self.joint_angles.get("左髋前摆", 0),
            "left_hip_side": self.joint_angles.get("左髋侧摆", 0),
            "left_knee": self.joint_angles.get("左膝", 0),
            "right_hip_forward": self.joint_angles.get("右髋前摆", 0),
            "right_hip_side": self.joint_angles.get("右髋侧摆", 0),
            "right_knee": self.joint_angles.get("右膝", 0),
            "is_zero": 1 if self.is_zero_condition else 0,
            "is_valid": 1
        }

        try:
            action_id = db_manager.insert_action(data)
            print(f"action_id: {action_id}")
            self.status_updated.emit(f"动作 '{action_name}' 保存成功，ID: {action_id}")
            print(f"Saved action {action_name} with ID: {action_id}")
        except Exception as e:
            self.status_updated.emit("保存动作失败！")
            print(f"Error saving action: {e}")



