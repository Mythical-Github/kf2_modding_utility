import sys
import json
from main import SETTINGS_JSON
from reusable_functions import *


with open(SETTINGS_JSON) as file:
    data = json.load(file)


# retrieving value from SETTINGS_JSON example
# server_ip = data["kf2_server_ip"]


sys.exit()
