import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'other', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

dir_path = data["kf2_docs_dir"]

os.startfile(dir_path)
