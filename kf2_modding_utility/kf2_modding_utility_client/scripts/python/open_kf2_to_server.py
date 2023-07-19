import sys
import json
import subprocess
from main import SETTINGS_JSON, DEV_SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    DATA = json.load(file)
    

with open(DEV_SETTINGS_JSON) as file:
    DEV_DATA = json.load(file)
    

STEAM_APP_ID = DEV_DATA["game_steam_app_id"]
SERVER_IP = DATA["kf2_server_ip"]
STEAM_EXE = DATA["steam_exe"]


subprocess.Popen([STEAM_EXE, "-applaunch", str(STEAM_APP_ID), "+connect", SERVER_IP])


sys.exit()
