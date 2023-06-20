import os
import json
import webbrowser

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'settings', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

url = data["vps_access_url"]

webbrowser.open(url)
