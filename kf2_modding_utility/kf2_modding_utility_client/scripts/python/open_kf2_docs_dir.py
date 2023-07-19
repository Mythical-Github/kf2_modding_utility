import sys
import json
from main import SETTINGS_JSON
from reusable_functions import *


with open(SETTINGS_JSON) as file:
    data = json.load(file)


DIR_PATH = data["kf2_docs_dir"]


open_dir_in_file_browser(DIR_PATH)


sys.exit()
