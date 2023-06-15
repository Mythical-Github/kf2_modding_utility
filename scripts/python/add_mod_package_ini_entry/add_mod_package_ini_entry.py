import json

def update_mod_packages(kf_editor_ini, mod_package_names_json):
    # Load JSON
    with open(mod_package_names_json, "r") as file:
        package_names = json.load(file)

    # Read the KFEditor.ini file
    with open(kf_editor_ini, "r") as file:
        lines = file.readlines()

    # Find the last ModPackages entry in the INI file
    last_mod_packages_index = -1
    for i, line in enumerate(lines):
        if line.startswith("ModPackages="):
            last_mod_packages_index = i

    # Check and add missing entries
    for package_name in package_names:
        mod_package_line = "ModPackages=" + package_name + "\n"
        if mod_package_line not in lines:
            lines.insert(last_mod_packages_index + 1, mod_package_line)

    # Write the updated INI file
    with open(kf_editor_ini, "w") as file:
        file.writelines(lines)

# Example usage
kf_editor_ini = "C:/Users/Mythical/Documents/GitHub/kf2_mythical/inis/KFEditor.ini"
mod_package_names_json = "C:/Users/Mythical/Documents/GitHub/kf2_mythical/scripts/python/add_mod_package_ini_entry/mod_package_names.json"
update_mod_packages(kf_editor_ini, mod_package_names_json)