import os
import json

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

dir_path = data["kf2_docs_dir"]

os.startfile(dir_path)
