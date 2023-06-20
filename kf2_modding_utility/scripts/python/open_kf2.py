import os
import json
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'settings', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

steam_app_id = data["game_steam_app_id"]
steam_exe = data["steam_exe"]

subprocess.Popen([steam_exe, "-applaunch", str(steam_app_id)])

quit()
