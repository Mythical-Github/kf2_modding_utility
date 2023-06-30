import os
import sys
import json
import socket
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'settings', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

content_brewer_py = f"{script_dir}\\brew_kf2_mods.py"
workshop_uploader_py = f"{script_dir}\\upload_mod_to_workshop_alt_method.py"
open_kf2_to_server_py = f"{script_dir}\\open_kf2_to_server.py"
server_restarter_py = f"{script_dir}\\restart_game_server.py"

host = data["kf2_server_ip"]
port = data["easy_testing_port"]

subprocess.run(["python", workshop_uploader_py])

subprocess.run(["python", server_restarter_py])

os.system("taskkill /f /im steam.exe")

os.system("taskkill /f /im KFGame.exe")

subprocess.Popen(["python", open_kf2_to_server_py])

sys.exit()
