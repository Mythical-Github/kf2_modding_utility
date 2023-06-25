import sys
import json
import subprocess
from pathlib import Path


def open_file_browser_to_dir(dir_path):
    if Path(dir_path).is_dir():
        if sys.platform.startswith('win'):
            subprocess.run(['explorer', dir_path], shell=True)
        elif sys.platform.startswith('linux'):
            subprocess.run(['xdg-open', dir_path])
        else:
            print("Unsupported platform.")
    else:
        print("Directory path is invalid or doesn't exist.")


def get_settings_value(input_key):
    settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'
    with open(settings_json) as file:
        data = json.load(file)
    output_value = data[input_key]
    return output_value


sys.exit()
