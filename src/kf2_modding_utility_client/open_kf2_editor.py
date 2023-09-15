import sys
import json
import subprocess
from main import CLIENT_SETTINGS_JSON

with open(CLIENT_SETTINGS_JSON) as file:
    dev_data = json.load(file)


STEAM_EXE = dev_data["steam_exe"]
STEAM_APP_ID = dev_data["editor_steam_app_id"]


command = [
    STEAM_EXE,
    "-applaunch",
    str(STEAM_APP_ID),
    "-NoGADWarning"
]


subprocess.Popen(command)


sys.exit()
