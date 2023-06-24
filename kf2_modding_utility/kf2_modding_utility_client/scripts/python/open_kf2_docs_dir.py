import json
import subprocess
import sys
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

dir_path = data["kf2_docs_dir"]

if Path(dir_path).is_dir():
    if sys.platform.startswith('win'):
        subprocess.run(['explorer', dir_path], shell=True)
    elif sys.platform.startswith('linux'):
        subprocess.run(['xdg-open', dir_path])
    else:
        print("Unsupported platform.")
else:
    print("Directory path is invalid or doesn't exist.")
