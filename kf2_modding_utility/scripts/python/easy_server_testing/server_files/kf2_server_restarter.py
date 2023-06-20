import os
import subprocess

kf2_dir = r"C:\game_servers\killing_floor_2"
task_name = "KFServer.exe"
os.system(f"taskkill /f /im {task_name}")
os.chdir(kf2_dir)
subprocess.run(r"C:\game_servers\killing_floor_2\KF2Server.bat")

quit()
