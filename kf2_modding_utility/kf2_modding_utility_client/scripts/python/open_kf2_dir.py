import os
import sys
import json
from pathlib import Path


settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

dir_path = data["kf2_game_dir"]


if dir_path and Path(dir_path).is_dir():
    if sys.platform.startswith('win'):
        os.startfile(dir_path)
    elif sys.platform.startswith('linux'):
        os.system(f'xdg-open "{dir_path}"')
    else:
        print("Unsupported platform.")
else:
    print("Directory path is invalid or doesn't exist.")

sys.exit()
