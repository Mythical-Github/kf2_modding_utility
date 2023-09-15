import sys
import json
from main import SETTINGS_JSON
from reusable_functions import *


with open(SETTINGS_JSON) as settings_json:
    SETTINGS_DATA = json.load(settings_json)
    
    
URL = SETTINGS_DATA["vps_access_url"]


open_website(URL)


sys.exit()
