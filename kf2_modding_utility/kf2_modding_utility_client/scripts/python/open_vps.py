import sys
import json
from main import SETTINGS_JSON
from reusable_functions import *


with open(SETTINGS_JSON) as settings_json:
    settings_data = json.load(settings_json)
    
    
url = settings_data["vps_access_url"]


open_website(url)


sys.exit()
