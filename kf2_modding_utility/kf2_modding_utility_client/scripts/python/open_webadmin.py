import sys
import json
import webbrowser
from pathlib import Path
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    data = json.load(file)


part_a = data["kf2_server_ip"]
part_b = data["webadmin_port"]
url = f"{part_a}:{part_b}"
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# using edge because wedadmin doesn't like firefox for me for whatever reason
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open(url)


sys.exit()
