import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    data = json.load(file)


ide_exe = data["ide_exe"]


subprocess.Popen([ide_exe])


sys.exit()
