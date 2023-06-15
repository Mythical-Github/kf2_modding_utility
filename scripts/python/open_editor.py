import subprocess

steam_exe = r"C:\Program Files (x86)\Steam\steam.exe"
steam_app_id = 232150

command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
    "-NoGADWarning"
]

subprocess.run(command)

quit()
