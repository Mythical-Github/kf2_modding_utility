import os
import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    data = json.load(file)


package_name = data["mod_package_name"]
part_a = data["kf2_game_dir"]
part_b = "Binaries/Win64"


kf2_dir = Path(part_a) / part_b


os.chdir(kf2_dir)


subprocess.Popen(["kfeditor", "brewcontent", "-platform=PC", package_name])


sys.exit()
