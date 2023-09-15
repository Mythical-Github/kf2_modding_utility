import sys
import json
import subprocess
from main import *
from pathlib import Path


# Loading various settings files
with open(CLIENT_SETTINGS_JSON) as file:
    data = json.load(file)
with open(DEV_CLIENT_SETTINGS_JSON) as file:
    dev_data = json.load(file)
with open(MUTATOR_CLIENT_SETTINGS_JSON) as file:
    mutators_data = json.load(file)
with open(GAME_MODE_CLIENT_SETTINGS_JSON) as file:
    game_mode_data = json.load(file)
with open(MAP_NAME_CLIENT_SETTINGS_JSON) as file:
    map_name_data = json.load(file)
with open(DIFFICULTY_CLIENT_SETTINGS_JSON) as file:
    difficulty_data = json.load(file)
with open(SEASONAL_ZED_CLIENT_SETTINGS_JSON) as file:
    seasonal_zeds_data = json.load(file)
with open(MATCH_LENGTH_CLIENT_SETTINGS_JSON) as file:
    match_length_data = json.load(file)


STEAM_EXE = data["steam_exe"]
STEAM_APP_ID = dev_data["game_steam_app_id"]


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


game_mode = game_mode_data["game_mode"][0]


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
    match_length = f"length={match_length}?"

    
seasonal_zeds = seasonal_zeds_data["seasonal_zeds"][0]


if not (seasonal_zeds == "" or seasonal_zeds is None):
    seasonal_zeds = f"AllowSeasonalSkins={seasonal_zeds}?"


subprocess.Popen(f"{STEAM_EXE} -applaunch {str(STEAM_APP_ID)} {map_name}{game_mode}{difficulty}{seasonal_zeds}{match_length}{mutators_line} -log")


sys.exit()
