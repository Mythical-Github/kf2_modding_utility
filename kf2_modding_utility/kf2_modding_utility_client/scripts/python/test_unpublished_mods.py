import sys
import json
import subprocess
from pathlib import Path

STEAM_APP_ID = 232090

settings_json = Path(__file__).resolve().parent.parent.parent / "settings" / "settings.json"
dev_settings_json = Path(__file__).resolve().parent.parent.parent / "settings" / "dev_settings.json"
mutators_settings_json = Path(__file__).resolve().parent.parent.parent / "settings" / "mutators.json"
game_mode_settings_json = Path(__file__).resolve().parent.parent.parent / "settings" / "game_mode.json"
map_name_settings = Path(__file__).resolve().parent.parent.parent / "settings" / "map_name.json"
difficulty_settings = Path(__file__).resolve().parent.parent.parent / "settings" / "match_difficulty.json"
seasonal_zeds_settings = Path(__file__).resolve().parent.parent.parent / "settings" / "seasonal_zeds.json"
match_length_settings = Path(__file__).resolve().parent.parent.parent / "settings" / "match_length.json"

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

with open(difficulty_settings) as file:
    difficulty_data = json.load(file)

with open(seasonal_zeds_settings) as file:
    seasonal_zeds_data = json.load(file)

with open(match_length_settings) as file:
    match_length_data = json.load(file)


steam_exe = data["steam_exe"]

mutators_line = ""
difficulty = ""
match_length = ""
seasonal_zeds = ""

if mutators_data["mutators"][0] == "" or mutators_data["mutators"][0] is None:
    print("test")
else:
    for mutator in mutators_data["mutators"]:
        if mutators_line == "":
            mutators_line = f"{mutator}"
        else:
            mutators_line = f"{mutators_line},{mutator}"

mutators_line = f"mutator={mutators_line}"

game_mode_key = "game_mode"

game_mode = f{game_mode_data[game_mode_key][0]"

if not (game_mode == "" or game_mode is None):
    game_mode = f"game={game_mode}?"
    

map_name = map_name_data["map_name"][0]

if map_name == "" or map_name is None:
    map_name = "KF-BioticsLab?"
else:
    map_name = f"{map_name}?"

difficulty = difficulty_data["match_difficulty"][0]

if not (difficulty == "" or difficulty is None):
    difficulty = f"difficulty={difficulty}?"
    
match_length = match_length_data["match_length"][0]

if not (match_length == "" or match_length is None):
    match_length = f"match_length={match_length}?"
    
seasonal_zeds = seasonal_zeds_data["seasonal_zeds"][0]

if not (seasonal_zeds == "" or seasonal_zeds is None):
    seasonal_zeds = f"seasonal_zeds={seasonal_zeds}?"

subprocess.Popen(f"{steam_exe} -applaunch {str(STEAM_APP_ID)} {map_name}{game_mode}{difficulty}{seasonal_zeds}{match_length}{mutators_line} -log -useunpublished")

sys.exit()
