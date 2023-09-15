import sys
import json
from main import CLIENT_SETTINGS_JSON
from reusable_functions import *


with open(CLIENT_SETTINGS_JSON) as file:
    data = json.load(file)


DIR_PATH = data["kf2_game_dir"]


open_dir_in_file_browser(DIR_PATH)


sys.exit()
