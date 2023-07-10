import sys
import json
import subprocess
from main import SETTINGS_JSON, DEV_SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    data = json.load(file)


with open(DEV_SETTINGS_JSON) as file:
    dev_data = json.load(file)


steam_exe = data["steam_exe"]
steam_app_id = dev_data["editor_steam_app_id"]


command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
    "-NoGADWarning"
]


subprocess.Popen(command)


sys.exit()
