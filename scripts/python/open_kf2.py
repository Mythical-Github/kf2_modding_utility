import subprocess

steam_app_id = 0

steam_exe = r""

subprocess.Popen([steam_exe, "-applaunch", steam_app_id])
