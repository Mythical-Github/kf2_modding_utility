import sys
import json
from reusable_functions import *
from main import SETTINGS_JSON, DEV_SETTINGS_JSON


with open(SETTINGS_JSON) as settings_json:
    settings_data = json.load(settings_json)


# retrieving value from SETTINGS_JSON example
# server_ip = settings_data["kf2_server_ip"]


with open(SETTINGS_JSON) as dev_settings_json:
    dev_settings_data = json.load(dev_settings_json)


sys.exit()
