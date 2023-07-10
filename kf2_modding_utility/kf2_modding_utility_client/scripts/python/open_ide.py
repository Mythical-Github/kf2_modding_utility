import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    data = json.load(file)


IDE_EXE = data["ide_exe"]


subprocess.Popen([IDE_EXE])


sys.exit()
