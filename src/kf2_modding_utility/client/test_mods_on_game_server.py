import os
import sys
import time
import subprocess


restart_delay = 10


content_brewer_py = f"{os.getcwd()}/brew_kf2_mods.py"
workshop_uploader_py = f"{os.getcwd()}/upload_mod_to_workshop_alt_method.py"
open_kf2_to_server_py = f"{os.getcwd()}/open_kf2_to_server.py"
server_restarter_py = f"{os.getcwd()}/restart_game_server.py"
close_kf2_py = f"{os.getcwd()}/close_kf2.py"
close_steam_py = f"{os.getcwd()}/close_steam.py"


subprocess.run(["python", workshop_uploader_py])
time.sleep(restart_delay)
subprocess.run(["python", server_restarter_py])
subprocess.run(["python", close_steam_py])
subprocess.run(["python", close_kf2_py])
time.sleep(restart_delay)
subprocess.run(["python", server_restarter_py])
subprocess.Popen(["python", open_kf2_to_server_py])


sys.exit()
