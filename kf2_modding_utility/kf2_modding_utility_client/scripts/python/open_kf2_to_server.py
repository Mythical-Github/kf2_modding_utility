import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'
with open(settings_json) as file:
    data = json.load(file)

steam_app_id = 232090
server_ip = data["kf2_server_ip"]

steam_exe = data["steam_exe"]

subprocess.Popen([steam_exe, "-applaunch", str(steam_app_id), "+connect", server_ip])
