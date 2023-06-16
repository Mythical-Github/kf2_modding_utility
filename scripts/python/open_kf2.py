import subprocess

steam_app_id = "232090"

steam_exe = r"C:\Program Files (x86)\Steam\Steam.exe"

subprocess.Popen([steam_exe, "-applaunch", steam_app_id])
