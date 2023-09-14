import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    DATA = json.load(file)


IDE_EXE = DATA["ide_exe"]


subprocess.Popen([IDE_EXE])


sys.exit()
