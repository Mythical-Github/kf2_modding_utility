import os
import json
import subprocess

# Get the absolute path of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to settings.json
settings_json = os.path.join(script_dir, '..', '..', 'settings', 'settings.json')

# Load JSON data from settings.json
with open(settings_json) as file:
    data = json.load(file)

ide_exe = data["ide_exe"]

# Run the blender_exe subprocess
subprocess.run([ide_exe])

quit()
