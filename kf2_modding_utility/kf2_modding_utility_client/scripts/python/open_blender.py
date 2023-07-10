import sys
import json
import subprocess
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    data = json.load(file)


blender_exe = data["blender_exe"]


subprocess.Popen([blender_exe])


sys.exit()
