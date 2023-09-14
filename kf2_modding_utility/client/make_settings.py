import sys
import json
from main import SETTINGS_JSON

SETTINGS = {
    "kf2_server_ip": "127.0.0.1",
    "mod_package_name": "Mythical",
    "mod_game_mode": "KFGameInfo_Mythical",
    "mod_map_name": "KF-ZedsDiner",
    "mod_mutator_name": "KF_Mutator_Mythical",
    "easy_testing_port": 7780,
    "webadmin_port": 7779,
    "game_port": 7777,
    "vps_access_url": "https:/remotedesktop.google.com/access/",
    "steam_exe": "C:/Program Files (x86)/Steam/steam.exe",
    "steam_cmd_exe": "C:/Programs/steamcmd/steamcmd.exe",
    "umodel_exe": "C:/Modding/Programs/Umodel/umodel_64.exe",
    "blender_exe": "C:/Program Files/Blender Foundation/Blender 3.5/blender.exe",
    "kf2_game_dir": "C:/Program Files (x86)/Steam/steamapps/common/killingfloor2",
    "kf2_docs_dir": "C:/Users/Mythical/Documents/My Games/KillingFloor2",
    "steam_username": "fake_username",
    "steam_password": "fake_password",
    "kf_editor_ini": "C:/Users/Mythical/Documents/My Games/KillingFloor2/KFGame/Config/KFEditor.ini",
    "ide_exe": "C:/Users/Mythical/AppData/Local/Programs/Microsoft VS Code/Code.exe",
    "publishedfileid": "0",
    "contentfolder": "C:/Users/Mythical/Documents/GitHub/kf2_mythical/kf2_modding_utility/scripts/python/upload_mod_to_workshop_alt_method/mod_upload_dir",
    "previewfile": "C:/Users/Mythical/Documents/GitHub/kf2_mythical/kf2_modding_utility/scripts/python/upload_mod_to_workshop_alt_method/Testing.png",
    "visibility": "0",
    "title": "Workshop Item Title Name",
    "description": "Workshop Item Description",
    "changenote": "Workshop Item Changenote Description",
    "show_log_window": "false"
}

with open(SETTINGS_JSON, 'w') as json_file:
    json.dump(SETTINGS, json_file, indent=4)  # Use json.dump, not json_file.dump

sys.exit()
