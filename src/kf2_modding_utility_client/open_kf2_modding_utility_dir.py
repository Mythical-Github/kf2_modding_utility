import sys
import json
from main import CLIENT_SETTINGS_JSON
from reusable_functions import *


with open(CLIENT_SETTINGS_JSON) as file:
    data = json.load(file)


DIR_PATH = Path(__file__).resolve().parent.parent.parent


open_dir_in_file_browser(DIR_PATH)


sys.exit()
