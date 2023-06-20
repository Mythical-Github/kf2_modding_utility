import sys
import json
import subprocess
import webbrowser
from PyQt5.QtGui import QColor, QLinearGradient, QIcon
from PyQt5.QtCore import QEvent, QObject, QSettings, QPoint
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QInputDialog, QScrollArea,
    QAction, QMenu
)

icon = r"..\..\images\kf2_icon_main.png"
title = "KF2 Modding Utility"
info_json = r"..\..\settings\data.json"
window_position_json = r"..\..\settings\window_position.json"

in_delete_state = False

scrollbox_buttons = []

style_1 = "background: #222222; color: white; border: 1px solid teal;"
style_2 = "background: #666666; color: white; border: 1px solid teal;"

def save_window_position_to_json(window):
    position = {
        'x': window.x(),
        'y': window.y(),
        'width': window.width(),
        'height': window.height()
    }
    with open(window_position_json, "w") as file:
        json.dump(position, file)

def load_data_from_json(json_file):
    with open(json_file) as file:
        return json.load(file)

def save_data_to_json(json_file, data):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def save_window_position(position):
    with open(window_position_json, "w") as file:
        json.dump(position, file)

def load_window_position():
    try:
        with open(window_position_json) as file:
            data = file.read().strip()
            if data:
                return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

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
        self.original_style = f"background: {gradient_str}; color: white; border: 1px solid teal;"
        self.setStyleSheet(self.original_style)

def create_button(title, path, highlightable=True):
    button = StyledButton(title, highlightable)
    button.clicked.connect(open_google)
    return button

def open_google():
    global in_delete_state
    if not in_delete_state:
        webbrowser.open("https://www.google.com")

def handle_file_selected(file_path, window):
    if file_path:
        name, ok = QInputDialog.getText(None, "Button Name", "Please Enter New Button Name:")
        if ok:
            data = load_data_from_json(info_json)
            new_button = {
                "title": name,
                "path": file_path
            }
            data.append(new_button)
            save_data_to_json(info_json, data)
            window_position = {
                'x': window.x(),
                'y': window.y(),
                'width': window.width(),
                'height': window.height()
            }
            save_window_position(window_position)
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()

def populate_scrollbox_buttons(layout):
    data = load_data_from_json(info_json)
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
    add_and_confirm_button = StyledButton("Add Button", highlightable=False)
    layout.addWidget(add_and_confirm_button)
    add_and_confirm_button.clicked.connect(on_add_and_confirm_button_clicked)

    remove_and_cancel_button = StyledButton("Remove Button(s)", highlightable=False)
    layout.addWidget(remove_and_cancel_button)
    remove_and_cancel_button.clicked.connect(lambda: toggle_confirm_button(add_and_confirm_button, remove_and_cancel_button))
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
            data = load_data_from_json(info_json)
            save_data_to_json(info_json, data)
            window_position = {
                'x': win.x(),
                'y': win.y(),
                'width': win.width(),
                'height': win.height()
            }
            save_window_position(window_position)
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()

def toggle_cancel_button(remove_and_cancel_button, scrollbox_buttons):
    if remove_and_cancel_button.text() == "Remove Button(s)":
        remove_and_cancel_button.setText("Cancel")
    else:
        remove_and_cancel_button.setText("Remove Button(s)")
        for button in scrollbox_buttons:
            button.setStylesheet()

def move_button_up(button):
    layout = button.parent()
    index = layout.indexOf(button)
    if index > 0:
        layout.insertLayout(index - 1, layout.takeAt(index))

def move_button_down(button):
    layout = button.parent()
    index = layout.indexOf(button)
    if index < layout.count() - 1:
        layout.insertLayout(index + 1, layout.takeAt(index))

class ModdingUtility(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(title)
        self.setStyleSheet("background-color: #111111;")
        layout = QVBoxLayout(self)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content = QWidget()
        scroll_area.setWidget(content)
        scroll_layout = QVBoxLayout(content)
        self.scrollbox_buttons = populate_scrollbox_buttons(scroll_layout)
        layout.addWidget(scroll_area)
        layout_top = QHBoxLayout()
        self.add_and_confirm_button, self.remove_and_cancel_button = create_top_scrollbox_buttons(layout_top, self.scrollbox_buttons)
        layout.addLayout(layout_top)
        self.remove_and_cancel_button.setCheckable(True)
        self.setLayout(layout)
        window_position = load_window_position()
        if window_position:
            self.setGeometry(window_position['x'], window_position['y'], window_position['width'], window_position['height'])
        else:
            self.resize(400, 300)

    def closeEvent(self, event):
        window_position = {
            'x': self.x(),
            'y': self.y(),
            'width': self.width(),
            'height': self.height()
        }
        save_window_position(window_position)
        event.accept()

def on_add_and_confirm_button_clicked():
    if in_delete_state:
        data = load_data_from_json(info_json)
        scrollbox_buttons_to_delete = []
        for button in scrollbox_buttons:
            if button.styleSheet() == style_2:
                scrollbox_buttons_to_delete.append(button)
        for button in scrollbox_buttons_to_delete:
            for item in data:
                if item['title'] == button.text():
                    data.remove(item)
        save_data_to_json(info_json, data)
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    else:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(None, "Select File", "", "Python Files (*.py);;All Files (*)", options=options)
        handle_file_selected(file_path, win)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon))
    win = ModdingUtility()
    win.show()
    sys.exit(app.exec_())
