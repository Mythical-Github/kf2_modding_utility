import os
import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    DATA = json.load(file)

kf2_dir = DATA["kf2_game_dir"]
kf2_dir = f"{kf2_dir}/Binaries/Win64"
os.chdir(kf2_dir)


subprocess.Popen(["kfeditor", "brewcontent", "-platform=PC", DATA["mod_package_name"]])


sys.exit()
