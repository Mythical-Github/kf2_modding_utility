import sys
import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

# Load JSON data from settings.json
with open(settings_json) as file:
    data = json.load(file)

ide_exe = data["ide_exe"]

# Run the blender_exe subprocess
subprocess.Popen([ide_exe])

sys.exit()
