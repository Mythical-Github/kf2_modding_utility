import json
import webbrowser

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

url = data["vps_access_url"]

webbrowser.open(url)
