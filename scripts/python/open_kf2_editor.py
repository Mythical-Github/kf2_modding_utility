import subprocess

steam_exe = r""
steam_app_id = 0

command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
    "-NoGADWarning"
]

subprocess.run(command)

quit()
