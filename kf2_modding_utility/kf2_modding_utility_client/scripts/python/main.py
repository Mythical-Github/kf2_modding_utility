import os
import sys
import time
import json
import subprocess
from PyQt5.QtGui import QColor, QLinearGradient, QIcon
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog,
                             QInputDialog, QScrollArea, QMessageBox
                             )


TITLE = "KF2 Modding Utility"
LAUNCHER_PY = "kf2_modding_utility_client.py"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
current_dir = os.getcwd()
ICON = os.path.normpath(os.path.join(current_dir, "..\\..\\images\\kf2_icon_main.png"))
INFO_JSON = os.path.normpath(os.path.join(current_dir, "..\\..\\settings\\button_data.json"))
WINDOW_POSITION_JSON = os.path.normpath(os.path.join(current_dir, "..\\..\\settings\\window_position.json"))
SETTINGS_JSON = os.path.normpath(os.path.join(current_dir, "..\\..\\settings\\settings.json"))


in_delete_state = False
scrollbox_buttons = []
color_1 = "color: white; border: 1px solid teal"
style_1 = f"background: #222222; {color_1};"
style_2 = f"background: #666666; {color_1};"
background_1 = "background-color: #111111;"


def execute_file(file_path):
    if not in_delete_state:
        subprocess.Popen([sys.executable, file_path])


def show_popup_message(message):
    msg_box = QMessageBox()
    msg_box.setWindowIcon(QIcon(ICON))
    msg_box.setText(message)
    msg_box.exec()


def settings_check():
    if not os.path.isfile(SETTINGS_JSON):
        execute_file("make_settings.py")
        execute_file("open_settings.py")
        show_popup_message("Please Configure And Save")
    return


def open_window_for_text_user_input(window_title_text, window_text):
    app = QApplication([])
    app.setWindowIcon(QIcon(ICON))

    ok = QInputDialog.getText(None, window_title_text, window_text)
    if ok[1]:
        output_text = ok[0]
    else:
        output_text = None

    return output_text


def save_window_position_to_json():
    position = {
        'x': win.x(),
        'y': win.y(),
        'width': win.width(),
        'height': win.height()
    }
    with open(WINDOW_POSITION_JSON, "w") as file:
        json.dump(position, file)


def load_data_from_json(json_file):
    with open(json_file) as file:
        return json.load(file)


def save_data_to_json(json_file, data):
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)


def load_window_position():
    try:
        with open(WINDOW_POSITION_JSON) as file:
            data = file.read().strip()
            if data:
                position = json.loads(data)
                return position
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def restart_app():
    save_window_position_to_json()
    win.close()
    os.chdir("../..")
    os.system(LAUNCHER_PY)
    quit()


class ButtonHoverEventFilter(QObject):
    def __init__(self, button):
        super().__init__(button)
        self.button = button
        self.original_style = button.styleSheet()

    def eventFilter(self, obj, event):
        if obj == self.button:
            if not in_delete_state and self.button.highlightable:
                if event.type() == QEvent.Enter:
                    self.button.setStyleSheet(style_1)
                elif event.type() == QEvent.Leave:
                    self.button.setStyleSheet(self.original_style)
                elif event.type() == QEvent.MouseButtonPress:
                    self.button.setStyleSheet(style_2)
                elif event.type() == QEvent.MouseButtonRelease:
                    self.button.setStyleSheet(self.original_style)
            elif in_delete_state and self.button.highlightable:
                if event.type() == QEvent.MouseButtonPress:
                    if self.button.styleSheet() == style_2:
                        self.button.setStyleSheet(self.original_style)
                    else:
                        self.button.setStyleSheet(style_2)
        return super().eventFilter(obj, event)


class StyledButton(QPushButton):
    def __init__(self, title, highlightable=True):
        super().__init__(title)
        self.setMinimumHeight(25)
        self.highlightable = highlightable
        self.original_style = ""
        self.setStylesheet()
        self.installEventFilter(ButtonHoverEventFilter(self))


    def setStylesheet(self):
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
        self.original_style = f"background: {gradient_str}; {color_1};"
        self.setStyleSheet(self.original_style)


def create_button(title, path, highlightable=True):
    button = StyledButton(title, highlightable)
    if path:
        button.clicked.connect(lambda checked, file_path=path: execute_file(file_path))
        button.clicked.connect(
            lambda checked, file_path=path: lambda: print(f"Path: {file_path}" if file_path else "Empty file path")())
    else:
        button.clicked.connect(lambda: print("Empty file path"))
    button.clicked.connect(lambda checked, button_title=title: print(f"Clicked button: {button_title}"))
    return button


def add_new_button(file_path):
    if file_path:
        name, ok = QInputDialog.getText(None, "Button Name", "Please Enter New Button Name:")
        if ok:
            data = load_data_from_json(INFO_JSON)
            new_button = {
                "title": name,
                "path": file_path
            }
            data.append(new_button)
            save_data_to_json(INFO_JSON, data)
            restart_app()


def populate_scrollbox_buttons(layout):
    data = load_data_from_json(INFO_JSON)
    for item in data:
        title_ = item['title']
        path = item['path']
        button_layout = QHBoxLayout()
        button = create_button(title_, path)
        button_layout.addWidget(button)
        layout.addLayout(button_layout)
        scrollbox_buttons.append(button)
    return scrollbox_buttons


def create_top_scrollbox_buttons(layout, scrollbox_buttons):
    add_and_confirm_button = StyledButton("Add Button", highlightable=True)
    layout.addWidget(add_and_confirm_button)
    add_and_confirm_button.clicked.connect(on_add_and_confirm_button_clicked)
    remove_and_cancel_button = StyledButton("Remove Button(s)", highlightable=True)
    layout.addWidget(remove_and_cancel_button)
    remove_and_cancel_button.clicked.connect(
        lambda: toggle_confirm_button(add_and_confirm_button, remove_and_cancel_button))
    remove_and_cancel_button.clicked.connect(lambda: toggle_cancel_button(remove_and_cancel_button, scrollbox_buttons))
    remove_and_cancel_button.setCheckable(True)
    return add_and_confirm_button, remove_and_cancel_button


def toggle_confirm_button(add_and_confirm_button, remove_and_cancel_button):
    global in_delete_state
    if remove_and_cancel_button.text() == "Remove Button(s)":
        add_and_confirm_button.setText("Confirm")
        in_delete_state = True
    else:
        add_and_confirm_button.setText("Add Button")
        in_delete_state = False
        if remove_and_cancel_button.isChecked():
            data = load_data_from_json(INFO_JSON)
            save_data_to_json(INFO_JSON, data)
            restart_app()


def toggle_cancel_button(remove_and_cancel_button, scrollbox_buttons):
    if remove_and_cancel_button.text() == "Remove Button(s)":
        remove_and_cancel_button.setText("Cancel")
    else:
        remove_and_cancel_button.setText("Remove Button(s)")
        for button in scrollbox_buttons:
            button.setStylesheet()


class ModdingUtility(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE)
        self.setStyleSheet(background_1)
        layout = QVBoxLayout(self)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content = QWidget()
        scroll_area.setWidget(content)
        scroll_layout = QVBoxLayout(content)
        self.scrollbox_buttons = populate_scrollbox_buttons(scroll_layout)
        layout.addWidget(scroll_area)
        layout_top = QHBoxLayout()
        self.add_and_confirm_button, self.remove_and_cancel_button = create_top_scrollbox_buttons(layout_top,
                                                                                                  self.scrollbox_buttons)
        layout.addLayout(layout_top)
        self.remove_and_cancel_button.setCheckable(True)
        self.setLayout(layout)
        window_position = load_window_position()
        if window_position:
            self.move(window_position['x'], window_position['y'])
            self.setFixedSize(window_position['width'], window_position['height'])
        else:
            self.move(window_position[0], window_position[0])
            self.setFixedSize(275, 400)


    def closeEvent(self, event):
        save_window_position_to_json()
        event.accept()


def on_add_and_confirm_button_clicked():
    if in_delete_state:
        data = load_data_from_json(INFO_JSON)
        scrollbox_buttons_to_delete = []
        for button in scrollbox_buttons:
            if button.styleSheet() == style_2:
                scrollbox_buttons_to_delete.append(button)
        for button in scrollbox_buttons_to_delete:
            for item in data:
                if item['title'] == button.text():
                    data.remove(item)
        save_data_to_json(INFO_JSON, data)
        restart_app()
    else:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(None, "Select File", "", "Python Files (*.py);;All Files (*)",
                                                   options=options)
        add_new_button(file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ICON))
    win = ModdingUtility()
    win.show()
    settings_check()
    sys.exit(app.exec_())
