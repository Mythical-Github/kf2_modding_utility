import sys
import json
import subprocess
from PyQt5.QtGui import QColor, QLinearGradient, QIcon
from PyQt5.QtCore import Qt, QEvent, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

title = "KF2 Modding Utility"
info_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\gui\data.json"

def run_script(path):
    subprocess.run(['python', path])

def populate_buttons(layout):
    with open(info_json) as json_file:
        data = json.load(json_file)

        for item in data:
            title = item['title']
            path = item['path']

            button = QPushButton(title)
            button.clicked.connect(lambda checked, p=path: run_script(p))

            # Set button's gradient background color
            gradient = QLinearGradient(0, 0, 0, 1)
            gradient.setColorAt(0, QColor(70, 70, 70))  # Dark grey
            gradient.setColorAt(1, QColor(128, 0, 0))  # Darker red

            gradient_stops = gradient.stops()
            gradient_str = "qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,"  # Flipped gradient

            for stop in gradient_stops:
                color = stop[1].darker(200).name()  # Make the red darker
                pos = 1 - stop[0]  # Reverse the position
                gradient_str += f" stop: {pos} {color},"

            gradient_str = gradient_str.rstrip(",") + ")"

            button.setStyleSheet(f"background: {gradient_str}; color: white; border: 1px solid teal;")
            button.setMinimumHeight(25)  # Set minimum height for the button

            button.installEventFilter(ButtonHoverEventFilter(button))  # Install event filter for hover effect

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
    
    # Set the icon of the window
    app.setWindowIcon(QIcon("kf2_icon.png"))
    
    window = QWidget()
    window.setWindowTitle(title)
    window.resize(275, 300)
    window.setStyleSheet("background-color: #111111;")  # Set the background color to dark black

    layout = QVBoxLayout()
    populate_buttons(layout)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
