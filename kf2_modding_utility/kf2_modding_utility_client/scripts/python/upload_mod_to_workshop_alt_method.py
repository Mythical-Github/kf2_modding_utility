import os
import re
import sys
import json
import subprocess
from pathlib import Path


SETTINGS_JSON = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(SETTINGS_JSON) as file:
    DATA = json.load(file)

KEYWORDS = {
    "publishedfileid",
    "contentfolder",
    "previewfile",
    "visibility",
    "title",
    "description",
    "changenote"
}

MOD_VDF = Path(__file__).resolve().parent.parent.parent / 'settings' / 'mod.vdf'
USERNAME = DATA["steam_username"]
PASSWORD = DATA["steam_password"]
STEAM_CMD_EXE = DATA["steam_cmd_exe"]


def replace_values_in_vdf(vdf_file, data):
    with open(vdf_file, 'r') as file:
        vdf_text = file.read()

    for key in data:
        pattern = rf'"{key}"\s+"([^"]*)"'
        replacement = f'"{key}" "{data[key]}"'
        vdf_text = re.sub(pattern, replacement, vdf_text)

    with open(vdf_file, 'w') as file:
        file.write(vdf_text)


replace_values_in_vdf(MOD_VDF, DATA)

subprocess.Popen(f"{STEAM_CMD_EXE} +login {USERNAME} {PASSWORD} +workshop_build_item {MOD_VDF} +quit")

sys.exit()
