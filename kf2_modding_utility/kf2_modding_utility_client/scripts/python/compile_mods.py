import sys
import json
import subprocess
from pathlib import Path
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    DATA = json.load(file)


kf2_dir = Path(DATA["kf2_game_dir"]) / "Binaries\Win64/kfeditor.exe"
command = [str(kf2_dir), "make"]


subprocess.Popen(command)


sys.exit()
