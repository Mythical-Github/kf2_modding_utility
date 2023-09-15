import sys
import json
import webbrowser
from main import CLIENT_SETTINGS_JSON


with open(CLIENT_SETTINGS_JSON) as file:
    DATA = json.load(file)


IP = DATA["kf2_server_ip"]
PORT = DATA["webadmin_port"]
url = f"{IP}:{PORT}"
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# using edge because wedadmin doesn't like firefox for me for whatever reason
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open(url)


sys.exit()
