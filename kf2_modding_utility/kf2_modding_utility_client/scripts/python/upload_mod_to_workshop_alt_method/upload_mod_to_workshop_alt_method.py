import time
import json
import re
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent.parent / 'settings' / 'settings.json'

keywords = {
    "publishedfileid",
    "contentfolder",
    "previewfile",
    "visibility",
    "title",
    "description",
    "changenote"
}

with open(settings_json) as file:
    data = json.load(file)

username = data["steam_username"]
password = data["steam_password"]
steam_cmd_exe = data["steam_cmd_exe"]
mod_vdf = data["mod_vdf"]


def replace_values_in_vdf(vdf_file, data):
    with open(vdf_file, 'r') as file:
        vdf_text = file.read()

    for key in data:
        pattern = rf'"{key}"\s+"([^"]*)"'
        replacement = f'"{key}" "{data[key]}"'
        vdf_text = re.sub(pattern, replacement, vdf_text)

    with open(vdf_file, 'w') as file:
        file.write(vdf_text)


replace_values_in_vdf(mod_vdf, data)

subprocess.Popen(f"{steam_cmd_exe} +login {username} {password} +workshop_build_item {mod_vdf} +quit")
