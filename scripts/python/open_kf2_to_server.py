import json
import subprocess

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

steam_app_id = data["game_steam_app_id"]
server_ip = data["kf2_server_ip"]

steam_exe = data["steam_exe"]

subprocess.Popen([steam_exe, "-applaunch", str(steam_app_id), "+connect", server_ip])
