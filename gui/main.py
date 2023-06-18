import sys
import json
import subprocess
from PyQt5.QtGui import QColor, QLinearGradient, QIcon
from PyQt5.QtCore import Qt, QEvent, QObject, QSettings
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

title = "KF2 Modding Utility"
info_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\gui\data.json"

def run_script(path):
    subprocess.run(['python', path])

def load_data_from_json(json_file):
    with open(json_file) as file:
        return json.load(file)

def populate_buttons(layout):
    data = load_data_from_json(info_json)

    for item in data:
        title = item['title']
        path = item['path']

        button = QPushButton(title)
        button.clicked.connect(lambda checked, p=path: run_script(p))

        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setColorAt(0, QColor(70, 70, 70))
        gradient.setColorAt(1, QColor(128, 0, 0))

        gradient_stops = gradient.stops()
        gradient_str = "qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,"

        for stop in gradient_stops:
            color = stop[1].darker(200).name()
            pos = 1 - stop[0]
            gradient_str += f" stop: {pos} {color},"

        gradient_str = gradient_str.rstrip(",") + ")"

        button.setStyleSheet(f"background: {gradient_str}; color: white; border: 1px solid teal;")
        button.setMinimumHeight(25)

        button.installEventFilter(ButtonHoverEventFilter(button))

        layout.addWidget(button)

class ButtonHoverEventFilter(QObject):
    def __init__(self, button):
        super().__init__(button)
        self.button = button
        self.original_style = button.styleSheet()

    def eventFilter(self, obj, event):
        if obj == self.button:
            if event.type() == QEvent.Enter:
                self.button.setStyleSheet("background: #222222; color: white; border: 1px solid teal;")
            elif event.type() == QEvent.Leave:
                self.button.setStyleSheet(self.original_style)

        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("kf2_icon_alt.png"))
    settings = QSettings("MyCompany", "KF2ModdingUtility")

    window = QWidget()
    window.setWindowTitle(title)
    window.resize(275, 300)
    window.setStyleSheet("background-color: #111111;")

    layout = QVBoxLayout()
    populate_buttons(layout)

    window.setLayout(layout)
    window_pos = settings.value("window_position", defaultValue=window.pos())
    window.move(window_pos)

    def save_window_position():
        settings.setValue("window_position", window.pos())

    window.show()
    app.aboutToQuit.connect(save_window_position)

    sys.exit(app.exec())
