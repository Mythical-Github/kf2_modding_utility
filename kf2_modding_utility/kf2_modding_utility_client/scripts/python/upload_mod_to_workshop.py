import os
import json
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

part_a = data["kf2_game_dir"]

os.chdir(part_a)
os.chdir("Binaries")

os.system(f"workshopusertool killing_floor_2_wsinfo_mod.txt")

quit()
