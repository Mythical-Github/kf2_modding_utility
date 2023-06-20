import os
import json
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'settings', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

part_a = data["kf2_game_dir"]
part_b = "Binaries\Win64"

kf2_dir = f"{part_a}\{part_b}"

os.chdir(kf2_dir)

subprocess.run(["kfeditor.exe", "make"])

quit()
