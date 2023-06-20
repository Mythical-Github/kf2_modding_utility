import os
import json
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'settings', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

umodel_exe = data["umodel_exe"]

kf2_dir = data["kf2_game_dir"]

os.chdir(kf2_dir)

subprocess.run([umodel_exe])

quit()
