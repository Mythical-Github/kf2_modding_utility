import sys
import time
import json
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


SETTINGS_DIR = Path(__file__).resolve().parent.parent.parent / "settings"


class ReusableButton(QPushButton):
    def __init__(self, title, value, click_callback):
        super().__init__(title)
        self.setMinimumHeight(25)
        self.value = value
        self.click_callback = click_callback
        self.setStylesheet()
        self.clicked.connect(self.handle_click)

    def setStylesheet(self):
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setColorAt(0, QColor(70, 70, 70))
        gradient.setColorAt(1, QColor(128, 0, 0))
        gradient_stops = gradient.stops()
        gradient_str = "qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,"
        color_1 = "color: white; border: 1px solid teal"
        self.original_style = f"background: {gradient_str}; {color_1};"
        for stop in gradient_stops:
            color = stop[1].darker(200).name()
            pos = 1 - stop[0]
            gradient_str += f" stop: {pos} {color},"
        gradient_str = gradient_str.rstrip(",") + ")"

        text_color = QColor(255, 255, 255)

        border_color = QColor(0, 128, 128)
        border_width = "1px"

        self.setStyleSheet(
            f"background: {gradient_str}; color: {text_color.name()};"
            f"border: {border_width} solid {border_color.name()};"
        )

    def handle_click(self):
        if self.click_callback:
            self.click_callback(self.text(), self.value)


class ValueDialog(QDialog):
    def __init__(self, key, current_value, settings_json, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Value")
        self.key = key
        self.current_value = current_value
        self.new_value = current_value
        self.settings_json = settings_json

        self.value_line_edit = QLineEdit()
        self.file_button = ReusableButton("Browse File", "", self.browse_file)
        self.dir_button = ReusableButton("Browse Directory", "", self.browse_directory)
        self.save_button = ReusableButton("Save", "", self.save_changes)
        self.save_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Editing value for key: {key}"))
        layout.addWidget(self.value_line_edit)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        layout.addLayout(button_layout)
        layout.addWidget(self.file_button)
        layout.addWidget(self.dir_button)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.setStyleSheet("color: white;")
        self.resize(400, 50)

        if isinstance(current_value, list):
            current_value = str(current_value)
        self.value_line_edit.setText(str(current_value))
        self.value_line_edit.textChanged.connect(self.value_changed)

    def value_changed(self, text):
        self.new_value = text
        self.save_button.setEnabled(True)

    def save_changes(self):
        with open(self.settings_json, 'r') as file:
            data = json.load(file)

        if isinstance(data[self.key], list):
            self.new_value = json.loads(self.new_value)
        data[self.key] = self.new_value

        with open(self.settings_json, 'w') as file:
            json.dump(data, file, indent=4)

        self.current_value = self.new_value
        self.save_button.setEnabled(False)

    def browse_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")

        if file_path:
            self.new_value = file_path
            self.value_line_edit.setText(file_path)
            self.value_changed(file_path)

    def browse_directory(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        dir_path = file_dialog.getExistingDirectory(self, "Select Directory")

        if dir_path:
            self.new_value = dir_path
            self.value_line_edit.setText(dir_path)
            self.value_changed(dir_path)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KF2 Modding Utility Settings Configurator")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)

        self.load_json_data(layout)

        self.setLayout(layout)
        self.setGeometry(450, 250, 275, 400)
        self.setStyleSheet("background-color: rgb(20, 20, 20);")

    def load_json_data(self, layout):
        json_files = [
            SETTINGS_DIR / "button_data.json",
            SETTINGS_DIR / "game_mode.json",
            SETTINGS_DIR / "map_name.json",
            SETTINGS_DIR / "match_difficulty.json",
            SETTINGS_DIR / "match_length.json",
            SETTINGS_DIR / "mod_package_names.json",
            SETTINGS_DIR / "mutators.json",
            SETTINGS_DIR / "seasonal_zeds.json",
            SETTINGS_DIR / "settings.json"
        ]

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_content.setLayout(scroll_layout)

        for json_file in json_files:
            with open(json_file) as file:
                try:
                    data = json.load(file)
                    print(f"JSON Data for {json_file}: {data}")
                    if isinstance(data, list):
                        self.add_list_scroll_area(scroll_layout, json_file.stem, data)
                    elif isinstance(data, dict):
                        self.add_button_group(scroll_layout, json_file.stem, data)
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON file: {json_file}")
                    print(e)
                    continue

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

    def add_button_group(self, layout, group_name, data):
        group_box = QGroupBox(group_name)
        group_layout = QVBoxLayout()
        group_box.setStyleSheet("color: white;")

        for item_key, item_value in data.items():
            button = ReusableButton(item_key, item_value, self.handle_button_click)
            group_layout.addWidget(button)

        group_box.setLayout(group_layout)
        layout.addWidget(group_box)

    def add_list_scroll_area(self, layout, group_name, data):
        group_box = QGroupBox(group_name)
        group_layout = QVBoxLayout()
        group_box.setStyleSheet("color: white;")

        scroll_area = QScrollArea()
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_content.setLayout(scroll_layout)

        for index, item_value in enumerate(data):
            button = ReusableButton(f"{item_value}", item_value, self.handle_button_click)
            scroll_layout.addWidget(button)

        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_content)
        group_layout.addWidget(scroll_area)
        group_box.setLayout(group_layout)
        layout.addWidget(group_box)

    def handle_button_click(self, key, current_value):
        settings_json = SETTINGS_DIR / f"{key}.json"
        dialog = ValueDialog(key, current_value, settings_json, self)

        if dialog.exec_():
            new_value = dialog.current_value
            sender_button = self.sender()
            sender_button.setText(new_value)

            with open(settings_json, 'r') as file:
                data = json.load(file)
                data[key] = new_value

            with open(settings_json, 'w') as file:
                json.dump(data, file, indent=4)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
