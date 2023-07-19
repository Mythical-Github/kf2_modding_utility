import re
import sys
import json
import subprocess
from main import SETTINGS_JSON, MOD_VDF


with open(SETTINGS_JSON) as file:
    SETTINGS_DATA = json.load(file)


KEYWORDS = {
    "publishedfileid",
    "contentfolder",
    "previewfile",
    "visibility",
    "title",
    "description",
    "changenote"
}


USERNAME = SETTINGS_DATA["steam_username"]
PASSWORD = SETTINGS_DATA["steam_password"]
STEAM_CMD_EXE = SETTINGS_DATA["steam_cmd_exe"]


def replace_values_in_vdf(vdf_file, data):
    with open(vdf_file, 'r') as file:
        vdf_text = file.read()

    for key in data:
        pattern = rf'"{key}"\s+"([^"]*)"'
        replacement = f'"{key}" "{data[key]}"'
        vdf_text = re.sub(pattern, replacement, vdf_text)

    with open(vdf_file, 'w') as file:
        file.write(vdf_text)


replace_values_in_vdf(MOD_VDF, SETTINGS_DATA)


subprocess.Popen(f"{STEAM_CMD_EXE} +login {USERNAME} {PASSWORD} +workshop_build_item {MOD_VDF} +quit")


sys.exit()
