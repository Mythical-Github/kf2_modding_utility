import json
import subprocess

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

umodel_exe = data["umodel_exe"]

subprocess.run([umodel_exe])

quit()
