import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPalette, QColor
import json
import subprocess
import os


test = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\gui\data.json"


def run_script(path):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.dwFlags |= subprocess.CREATE_NO_WINDOW
    subprocess.run(['python', path], startupinfo=startupinfo)


def populate_buttons(layout):
    with open(test) as json_file:
        data = json.load(json_file)

        for item in data:
            title = item['title']
            path = item['path']

            button = QPushButton(title)
            button.clicked.connect(lambda checked, p=path: run_script(p))
            layout.addWidget(button)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Set Dracula theme stylesheet
    app.setStyle("Fusion")

    # Dracula color palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(40, 42, 54))
    palette.setColor(QPalette.WindowText, QColor(248, 248, 242))
    palette.setColor(QPalette.Base, QColor(68, 71, 90))
    palette.setColor(QPalette.AlternateBase, QColor(62, 66, 82))
    palette.setColor(QPalette.ToolTipBase, QColor(248, 248, 242))
    palette.setColor(QPalette.ToolTipText, QColor(248, 248, 242))
    palette.setColor(QPalette.Text, QColor(248, 248, 242))
    palette.setColor(QPalette.Button, QColor(68, 71, 90))
    palette.setColor(QPalette.ButtonText, QColor(248, 248, 242))
    palette.setColor(QPalette.BrightText, QColor(255, 80, 123))
    palette.setColor(QPalette.Link, QColor(189, 147, 249))
    palette.setColor(QPalette.Highlight, QColor(189, 147, 249))
    palette.setColor(QPalette.HighlightedText, QColor(40, 42, 54))
    app.setPalette(palette)

    window = QWidget()
    window.setWindowTitle('KF2 Modding Utility')  # Set the new title
    window.resize(275, 300)  # Adjust the window width as needed

    layout = QVBoxLayout()
    populate_buttons(layout)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
