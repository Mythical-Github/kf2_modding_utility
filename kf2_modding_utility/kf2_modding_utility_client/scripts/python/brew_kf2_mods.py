import sys
import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

package_name = data["mod_package_name"]
part_a = data["kf2_game_dir"]
part_b = "Binaries/Win64"

kf2_dir = Path(part_a) / part_b

subprocess.Popen(["kfeditor", "brewcontent", "-platform=PC", package_name], cwd=kf2_dir)

sys.exit()
