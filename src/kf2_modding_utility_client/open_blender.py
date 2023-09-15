import sys
import json
import subprocess
from main import CLIENT_SETTINGS_JSON


with open(CLIENT_SETTINGS_JSON) as file:
    DATA = json.load(file)


BLENDER_EXE = DATA["blender_exe"]


subprocess.Popen([BLENDER_EXE])


sys.exit()
