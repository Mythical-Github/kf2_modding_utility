import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    DATA = json.load(file)


BLENDER_EXE = DATA["blender_exe"]


subprocess.Popen([BLENDER_EXE])


sys.exit()
