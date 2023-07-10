import sys
import json
import subprocess
from main import *


with open(SETTINGS_JSON) as file:
    data = json.load(file)


with open(DEV_SETTINGS_JSON) as file:
    dev_data = json.load(file)


STEAMP_APP_ID = dev_data["game_steam_app_id"]
STEAM_EXE = data["steam_exe"]


subprocess.Popen([STEAM_EXE, "-applaunch", str(STEAM_APP_ID)])


sys.exit()
