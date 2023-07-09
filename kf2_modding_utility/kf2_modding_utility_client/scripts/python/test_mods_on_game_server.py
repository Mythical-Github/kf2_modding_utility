import os
import sys
import json
import time
import socket
import subprocess

restart_delay = 20

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

print("workshop uploader started")
subprocess.run(["python", workshop_uploader_py])
print("workshop uploader finished")

print("first server restart started")
subprocess.run(["python", server_restarter_py])
print("first server restart ended")

os.system("taskkill /f /im steam.exe")

os.system("taskkill /f /im KFGame.exe")

print("started delay")
time.sleep(restart_delay)
print("delay ended")

print("second server restart started")
subprocess.run(["python", server_restarter_py])
print("second server restart ended")

print("started opening game to server")
subprocess.Popen(["python", open_kf2_to_server_py])
print("end of opening game to server")

sys.exit()
