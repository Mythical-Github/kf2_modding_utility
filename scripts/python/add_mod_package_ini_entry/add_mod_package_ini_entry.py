import json


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

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'other', 'settings.json')

kf_editor_ini = ""
mod_package_names_json = os.path.join(script_dir, "..", "..", "..", "scripts", "python", "add_mod_package_ini_entry", "mod_package_names.json")
update_mod_packages(kf_editor_ini, mod_package_names_json)

quit()
