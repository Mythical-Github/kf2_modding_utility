import os
import json
import time
import shutil
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'
template = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings_examples' / 'example_upload_info.txt'


with open(settings_json) as file:
    data = json.load(file)

part_a = data["kf2_game_dir"]

os.chdir(part_a)
os.chdir("Binaries")


test = data["kf2_docs_dir"]

testing = f'{test}\\killing_floor_2_wsinfo_mod.txt'

testing = Path(testing)

if os.path.isfile(testing):
    testing.unlink()

wsinfo_file = f"{test}\\killing_floor_2_wsinfo_mod.txt"

with open(wsinfo_file, 'w') as file:
    pass

with open(wsinfo_file, 'a') as file:
    file.write(f'$Description "{data["description"]}"\n')
    file.write(f'$Title "{data["title"]}"\n')
    file.write(f'$PreviewFile "{data["previewfile"]}"\n')
    file.write(f'$Tags ""\n')
    file.write(f'$MicroTxItem "false"\n')
    file.write(f'$PackageDirectory "{data["contentfolder"]}"\n')
    pass

os.system(f"workshopusertool killing_floor_2_wsinfo_mod.txt")

quit()
