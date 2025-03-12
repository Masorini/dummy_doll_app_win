from app.core.controller.realtime_controller import RealtimeController
from app.core.pages.realtime import RealtimePage
from app.core.connector.page_connector import PageConnector

class RealtimeConnector(PageConnector):
    def __init__(self, page: RealtimePage, controller: RealtimeController):
        super().__init__(page, controller)
        self.init_connector()

    def init_connector(self):
        self.page.power_on_btn.clicked.connect(self.controller.power_on)
        self.page.execute_btn.clicked.connect(self.controller.execute)
        self.page.stop_btn.clicked.connect(self.controller.stop)

        self.page.bpm_slider.valueChanged.connect(self.controller.set_breathing_rate)
        self.page.amp_slider.valueChanged.connect(self.controller.set_breathing_amplitude)
        self.page.hr_slider.valueChanged.connect(self.controller.set_heartbeat_rate)

        self.page.action_combo.currentTextChanged.connect(self.controller.select_action)

        self.page.load_btn.clicked.connect(self.controller.load_configuration)

        self.controller.breathing_rate_changed.connect(lambda value: self.page.bpm_label.setText(f"{value} bpm"))
        self.controller.breathing_amplitude_changed.connect(lambda value: self.page.amp_label.setText(f"{value} mm"))
        self.controller.heartbeat_rate_changed.connect(lambda value: self.page.hr_label.setText(f"{value} bpm"))
