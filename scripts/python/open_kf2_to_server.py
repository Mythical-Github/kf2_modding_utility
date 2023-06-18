import subprocess

steam_app_id = 0
server_ip = ""

steam_exe = r""

subprocess.Popen([steam_exe, "-applaunch", steam_app_id, "+connect", server_ip])
