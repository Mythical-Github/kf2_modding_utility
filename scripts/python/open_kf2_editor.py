import json
import subprocess

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

steam_exe = data["steam_exe"]
steam_app_id = data["editor_steam_app_id"]

command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
    "-NoGADWarning"
]

subprocess.run(command)

quit()
