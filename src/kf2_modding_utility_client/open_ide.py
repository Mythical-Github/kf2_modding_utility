import sys
import json
import subprocess
from main import CLIENT_SETTINGS_JSON


with open(CLIENT_SETTINGS_JSON) as file:
    DATA = json.load(file)


IDE_EXE = DATA["ide_exe"]


subprocess.Popen([IDE_EXE])


sys.exit()
