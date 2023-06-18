import os
import json
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'other', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

steam_app_id = data["game_steam_app_id"]
server_ip = data["kf2_server_ip"]

steam_exe = data["steam_exe"]

subprocess.Popen([steam_exe, "-applaunch", str(steam_app_id), "+connect", server_ip])
