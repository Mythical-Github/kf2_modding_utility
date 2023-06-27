import sys
import json
import subprocess
from pathlib import Path


def get_settings_value(input_key):
    settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'
    with open(settings_json) as file:
        data = json.load(file)
    output_value = data[input_key]
    return output_value


sys.exit()
