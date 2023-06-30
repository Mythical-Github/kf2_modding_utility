import sys
import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'
dev_settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'dev_settings.json'
mutators_settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'mutators.json'
game_mode_settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'game_mode.json'
map_name_settings = Path(__file__).resolve().parent.parent.parent / 'settings' / 'map_name.json'

with open(settings_json) as file:
    data = json.load(file)

with open(dev_settings_json) as file:
    dev_data = json.load(file)

with open(mutators_settings_json) as file:
    mutators_data = json.load(file)

with open(game_mode_settings_json) as file:
    game_mode_data = json.load(file)

with open(map_name_settings) as file:
    map_name_data = json.load(file)

mutators_line = ""

steam_exe = data["steam_exe"]
steam_app_id = dev_data["game_steam_app_id"]

if mutators_data['mutators'][0] == "" or mutators_data['mutators'][0] is None:
    print("test")
else:
    for mutator in mutators_data['mutators']:
        if mutators_line == "":
            mutators_line = f"{mutator}"
        else:
            mutators_line = f"{mutators_line},{mutator}"


mutators_line = f"mutator={mutators_line}"




game_mode_key = "game_mode"  # Use a different variable name

if game_mode_key == "" or game_mode_key is None:
    game_mode = ""
else:
    game_mode = f"{game_mode_data[game_mode_key][0]}?"  # Access value using the correct variable

game_mode = f"game={game_mode}"

map_name_key = "map_name"  # Add a variable to hold the key for map_name

map_name = map_name_data[map_name_key][0]  # Access value using the correct variable

if map_name == "" or map_name is None:
    map_name = "KF-BioticsLab"

command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
    map_name,
    game_mode,
    mutators_line,
    "-log",
    "-useunpublished"
]

subprocess.Popen(command)

sys.exit()
