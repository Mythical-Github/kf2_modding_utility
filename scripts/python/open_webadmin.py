import json
import webbrowser

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

part_a = data["kf2_server_ip"]
part_b =data["webadmin_port"]
url = f"{part_a}:{part_b}"
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

#using edge because wedadmin doesn't like firefox for me for whatever reason
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open(url)
