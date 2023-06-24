import os
import json
import socket
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', '..', 'settings', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

content_brewer_py = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\kf2_modding_utility\scripts\python\brew_kf2_mods.py"
workshup_uploader_py = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\kf2_modding_utility\scripts\python\upload_mod_to_workshop_alt_method\upload_mod_to_workshop_alt_method.py"
open_kf2_to_server_py = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\kf2_modding_utility\scripts\python\open_kf2_to_server.py"

host = data["kf2_server_ip"]
port = data["easy_testing_port"]

subprocess.run(["python", workshup_uploader_py])

command_to_send = 'restart_server'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

client_socket.sendall(command_to_send.encode())

client_socket.close()

os.system("taskkill /f /im steam.exe")

subprocess.Popen(["python", open_kf2_to_server_py])
