import json
import subprocess

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

blender_exe = data["blender_exe"]

subprocess.run([blender_exe])

quit()
