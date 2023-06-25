import os
import json
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtGui import QIcon

settings_json = Path(__file__).resolve().parent.parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

icon_path = data["icon_path"]

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

window_title = 'Add Mod Package Name To Ini'
window_text = 'Enter New Mod Package Name'

user_input = open_window_for_text_user_input(window_title, window_text)

ini_json = f"{os.getcwd()}\\add_mod_package_ini_entry\\mod_package_names.json"
print(ini_json)

def save_data_to_json(json_file, data):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

with open(ini_json) as file_:
    ini_data = json.load(file_)
    ini_data.append(user_input)
    save_data_to_json(ini_json, ini_data)

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


script_dir = Path(__file__).resolve().parent
settings_json = Path(__file__).resolve().parent.parent.parent.parent / 'settings' / 'settings.json'



with open(settings_json) as file:
    data = json.load(file)

kf_editor_ini = data["kf_editor_ini"]
mod_package_names_json = script_dir.parent / "add_mod_package_ini_entry" / "mod_package_names.json"

update_mod_packages(kf_editor_ini, mod_package_names_json)

quit()
