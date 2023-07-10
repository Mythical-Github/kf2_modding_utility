import json

data = {
    "kf2_server_ip": "127.0.0.1",
    "mod_package_name": "Mythical",
    "mod_game_mode": "KFGameInfo_Mythical",
    "mod_map_name": "KF-ZedsDiner",
    "mod_mutator_name": "KF_Mutator_Mythical",
    "easy_testing_port": 7780,
    "webadmin_port": 7779,
    "game_port": 7777,
    "vps_access_url": "https://remotedesktop.google.com/access/",
    "steam_exe": r"C:\\Program Files (x86)\\Steam\\steam.exe",
    "steam_cmd_exe": r"C:\\Programs\\steamcmd\\steamcmd.exe",
    "umodel_exe": r"C:\\Modding\\Programs\\Umodel\\umodel_64.exe",
    "blender_exe": r"C:\\Program Files\\Blender Foundation\\Blender 3.5\\blender.exe",
    "kf2_game_dir": r"C:\\Program Files (x86)\\Steam\\steamapps\\common\\killingfloor2",
    "kf2_docs_dir": r"C:\\Users\\Mythical\\Documents\\My Games\\KillingFloor2",
    "steam_username": "fake_username",
    "steam_password": "fake_password",
    "kf_editor_ini": r"C:\\Users\\Mythical\\Documents\\My Games\\KillingFloor2\\KFGame\\Config\\KFEditor.ini",
    "ide_exe": "C:\\Users\\Mythical\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "publishedfileid": "0",
    "contentfolder": "C:/Users/Mythical/Documents/GitHub/kf2_mythical/kf2_modding_utility/scripts/python/upload_mod_to_workshop_alt_method/mod_upload_dir",
    "previewfile": "C:/Users/Mythical/Documents/GitHub/kf2_mythical/kf2_modding_utility/scripts/python/upload_mod_to_workshop_alt_method/Testing.png",
    "visibility": "0",
    "title": "Workshop Item Title Name",
    "description": "Workshop Item Description",
    "changenote": "Workshop Item Changenote Description",
    "show_log_window": "false"
}

with open('..\\..\\settings\\settings.json', 'w') as file:
    json.dump(data, file, indent=4)
