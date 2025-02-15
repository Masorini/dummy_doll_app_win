from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit

class ParameterInput(QWidget):
    def __init__(self, label, unit, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.label = QLabel(f"{label}:")
        self.input = QLineEdit()
        self.unit = QLabel(unit)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.unit)
        self.setLayout(layout)