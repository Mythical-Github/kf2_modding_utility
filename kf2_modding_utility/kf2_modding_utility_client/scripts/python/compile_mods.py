import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    data = json.load(file)


part_a = data["kf2_game_dir"]
part_b = "Binaries\Win64"


kf2_dir = Path(part_a) / part_b


subprocess.Popen([kf2_dir / "kfeditor.exe", "make"])


sys.exit()
