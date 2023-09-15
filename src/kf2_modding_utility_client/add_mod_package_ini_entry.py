import json
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import CLIENT_SETTINGS_JSON


with open(CLIENT_SETTINGS_JSON) as file:
    data = json.load(file)
with open(DEV_CLIENT_SETTINGS_JSON) as file:
    dev_data = json.load(file)
with open(MOD_PACKAGE_NAMES_JSON) as file_:
    ini_data = json.load(file_)
    ini_data.append(user_input)
    save_data_to_json(MOD_PACKAGE_NAMES_JSON, ini_data)


icon_path = dev_data["icon_path"]
kf_editor_ini = data["kf_editor_ini"]
window_text = 'Enter New Mod Package Name'
window_title = 'Add Mod Package Name To Ini'
user_input = open_window_for_text_user_input(window_title, window_text)


def open_window_for_text_user_input(window_title_text, window_text):
    app = QApplication([])
    app.setWindowIcon(QIcon(icon_path))
    dialog = QInputDialog()
    dialog.setWindowTitle(window_title_text)
    dialog.setLabelText(window_text)
    dialog.resize(350, dialog.height())
    ok = dialog.exec_()


    if ok:
        output_text = dialog.textValue()
    else:
        output_text = None

    return output_text


def save_data_to_json(json_file, data):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


def update_mod_packages(kf_editor_ini, mod_package_names_json):
    with open(mod_package_names_json, "r") as file:
        package_names = json.load(file)


    with open(kf_editor_ini, "r") as file:
        lines = file.readlines()


    last_mod_packages_index = -1
    for i, line in enumerate(lines):
        if line.startswith("ModPackages="):
            last_mod_packages_index = i


    for package_name in package_names:
        mod_package_line = "ModPackages=" + package_name + "\n"
        if mod_package_line not in lines:
            lines.insert(last_mod_packages_index + 1, mod_package_line)


    with open(kf_editor_ini, "w") as file:
        file.writelines(lines)


update_mod_packages(kf_editor_ini, MOD_PACKAGE_NAMES_JSON)


quit()
