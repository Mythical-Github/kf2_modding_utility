import os
import json

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

package_name = data["mod_package_name"]
part_a = data["kf2_game_dir"]
part_b = "Binaries\Win64"

kf2_dir = f"{part_a}\{part_b}"
print(kf2_dir)

os.chdir(kf2_dir)
os.system(f"kfeditor brewcontent -platform=PC {package_name}")

quit()
