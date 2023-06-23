import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

steam_app_id = data["game_steam_app_id"]
steam_exe = data["steam_exe"]

subprocess.Popen([steam_exe, "-applaunch", str(steam_app_id)])

quit()
