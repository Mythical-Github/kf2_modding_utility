import json
import subprocess

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

steam_exe = data["steam_exe"]
package_name = data["mod_package_name"]
game_mode = data["mod_game_mode"]
map_name = data["mod_map_name"]
mutator_name = data["mod_mutator_name"]
steam_app_id = data["game_steam_app_id"]

command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
    f"{map_name}?game={package_name}.{game_mode}?mutator={package_name}.{mutator_name},ServerExtMut.ServerExtMut",
    "-log"
]

subprocess.run(command)

quit()
