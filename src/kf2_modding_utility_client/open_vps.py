import sys
import json
from main import CLIENT_SETTINGS_JSON
from reusable_functions import *


with open(CLIENT_SETTINGS_JSON) as settings_json:
    SETTINGS_DATA = json.load(settings_json)
    
    
URL = SETTINGS_DATA["vps_access_url"]


open_website(URL)


sys.exit()
