import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

umodel_exe = data["umodel_exe"]
kf2_dir = data["kf2_game_dir"]

subprocess.Popen([umodel_exe], cwd=kf2_dir, shell=True)
