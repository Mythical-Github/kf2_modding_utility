import os
import json
from pathlib import Path
from main import CLIENT_SETTINGS_JSON


with open(CLIENT_SETTINGS_JSON) as file:
    settings_data = json.load(file)


kf2_docs_dir = settings_data["kf2_game_dir"]
template = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings_examples' / 'example_upload_info.txt'
wsinfo_file = f"{kf2_docs_dir}\\killing_floor_2_wsinfo_mod.txt"
wsinfo_file = Path(wsinfo_file)


os.chdir(f"{kf2_docs_dir}/Binaries")


if os.path.isfile(wsinfo_file):
    wsinfo_file.unlink()


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
