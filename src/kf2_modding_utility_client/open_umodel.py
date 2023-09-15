import sys
import json
import subprocess
from main import CLIENT_SETTINGS_JSON


with open(CLIENT_SETTINGS_JSON) as file:
    data = json.load(file)


UMODEL_EXE = data["umodel_exe"]
KF2_GAME_DIR = data["kf2_game_dir"]


subprocess.Popen([UMODEL_EXE], cwd=KF2_GAME_DIR, shell=True)


sys.exit()
