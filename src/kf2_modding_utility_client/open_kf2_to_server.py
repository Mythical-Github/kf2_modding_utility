import sys
import json
import subprocess
from main import CLIENT_SETTINGS_JSON

with open(CLIENT_SETTINGS_JSON) as file:
    dev_data = json.load(file)

STEAM_APP_ID = dev_data["game_steam_app_id"]
STEAM_EXE = dev_data["steam_exe"]
SERVER_IP = dev_data["kf2_server_ip"]
SERVER_PORT = dev_data["game_port"]
FULL_ADDRESS = f"{SERVER_IP}:{SERVER_PORT}"

subprocess.Popen([STEAM_EXE, "-applaunch", str(STEAM_APP_ID), "+connect", FULL_ADDRESS])

sys.exit()
