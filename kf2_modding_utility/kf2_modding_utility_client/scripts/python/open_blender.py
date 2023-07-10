import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    data = json.load(file)


BLENDER_EXE = data["BLENDER_EXE"]


subprocess.Popen([BLENDER_EXE])


sys.exit()
