import sys
import json
import subprocess
from main import CLIENT_SETTINGS_JSON

with open(CLIENT_SETTINGS_JSON) as file:
    dev_data = json.load(file)


STEAM_APP_ID = dev_data["game_steam_app_id"]
STEAM_EXE = dev_data["steam_exe"]


subprocess.Popen([STEAM_EXE, "-applaunch", str(STEAM_APP_ID)])


sys.exit()
