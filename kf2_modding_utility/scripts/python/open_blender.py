import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

blender_exe = data["blender_exe"]

subprocess.Popen([blender_exe])

quit()
