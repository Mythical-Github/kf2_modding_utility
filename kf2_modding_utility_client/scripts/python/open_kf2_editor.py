import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

steam_exe = data["steam_exe"]
steam_app_id = data["editor_steam_app_id"]

command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
    "-NoGADWarning"
]

subprocess.Popen(command)

quit()
