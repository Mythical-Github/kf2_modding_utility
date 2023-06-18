import os
import json
import subprocess

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

umodel_exe = data["umodel_exe"]

kf2_dir = data["kf2_game_dir"]

os.chdir(kf2_dir)

subprocess.run([umodel_exe])

quit()
