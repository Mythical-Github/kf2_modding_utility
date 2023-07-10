import os
import json
import time
import shutil
from pathlib import Path
from main import SETTINGS_JSON


template = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings_examples' / 'example_upload_info.txt'
wsinfo_file = f"{test}\\killing_floor_2_wsinfo_mod.txt"


with open(SETTINGS_JSON) as file:
    settings_data = json.load(file)


part_a = settings_data["kf2_game_dir"]


os.chdir(part_a)
os.chdir("Binaries")


testing = f'{test}\\killing_floor_2_wsinfo_mod.txt'


testing = Path(testing)


if os.path.isfile(testing):
    testing.unlink()


with open(wsinfo_file, 'w') as file:
    pass


with open(wsinfo_file, 'a') as file:
    file.write(f'$Description "{settings_data["description"]}"\n')
    file.write(f'$Title "{settings_data["title"]}"\n')
    file.write(f'$PreviewFile "{settings_data["previewfile"]}"\n')
    file.write(f'$Tags ""\n')
    file.write(f'$MicroTxItem "false"\n')
    file.write(f'$PackageDirectory "{settings_data["contentfolder"]}"\n')
    pass


os.system(f"workshopusertool killing_floor_2_wsinfo_mod.txt")


quit()
