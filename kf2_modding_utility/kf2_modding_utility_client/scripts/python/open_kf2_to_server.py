import sys
import json
import subprocess
from pathlib import Path


SETTINGS_JSON = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'
STEAM_APP_ID = 232090
SERVER_IP = data["kf2_SERVER_IP"]
STEAM_EXE = data["STEAM_EXE"]


with open(SETTINGS_JSON) as file:
    data = json.load(file)


subprocess.Popen([STEAM_EXE, "-applaunch", str(STEAM_APP_ID), "+connect", SERVER_IP])


sys.exit()
