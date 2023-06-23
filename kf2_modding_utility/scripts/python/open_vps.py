import json
import webbrowser
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

url = data["vps_access_url"]

webbrowser.open(url)
