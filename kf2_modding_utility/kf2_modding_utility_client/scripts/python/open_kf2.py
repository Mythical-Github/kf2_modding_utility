import sys
import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'
dev_settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'dev_settings.json'

with open(settings_json) as file:
    data = json.load(file)

with open(dev_settings_json) as file:
    dev_data = json.load(file)

steam_app_id = dev_data["game_steam_app_id"]
steam_exe = data["steam_exe"]

subprocess.Popen([steam_exe, "-applaunch", str(steam_app_id)])

sys.exit()
