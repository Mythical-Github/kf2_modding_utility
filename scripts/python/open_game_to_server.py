import subprocess

steam_exe = r"C:\Program Files (x86)\Steam\steam.exe"
server_ip = ""
steam_app_id = 232090

command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
#    f"connect={server_ip}"
#    f"open {server_ip}"
]

subprocess.run(command)

quit()
