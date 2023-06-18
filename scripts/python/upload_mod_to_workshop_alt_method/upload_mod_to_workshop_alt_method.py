import json
import subprocess

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

username = data["steam_username"]
password = data["steam_password"]
steam_cmd_exe = data["steam_cmd_exe"]
mod_vdf = data["mod_vdf"]

subprocess.run(f"{steam_cmd_exe} +login {username} {password} +workshop_build_item {mod_vdf} +quit")