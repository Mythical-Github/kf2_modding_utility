import json

data_2 = {
    "kf2_server_ip": "127.0.0.1",
    "mod_package_name": "Mythical",
    "mod_game_mode": "KFGameInfo_Mythical",
    "mod_map_name": "KF-ZedsDiner",
    "mod_mutator_name": "KF_Mutator_Mythical",
    "game_steam_app_id": 232090,
    "editor_steam_app_id": 232150,
    "easy_testing_port": 7780,
    "webadmin_port": 7779,
    "game_port": 7777,
    "vps_access_url": "https://remotedesktop.google.com/access/",
    "steam_exe": r"C:\Program Files (x86)\Steam\steam.exe",
    "steam_cmd_exe": r"C:\Programs\steamcmd\steamcmd.exe",
    "umodel_exe": r"C:\Modding\Programs\Umodel\umodel_64.exe",
    "blender_exe": r"C:\Program Files\Blender Foundation\Blender 3.5\blender.exe",
    "kf2_game_dir": r"C:\Program Files (x86)\Steam\steamapps\common\killingfloor2",
    "kf2_docs_dir": r"C:\Users\Mythical\Documents\My Games\KillingFloor2",
    "steam_username": "fake_username",
    "steam_password": "fake_password",
    "mod_vdf": r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\scripts\python\upload_mod_to_workshop_alt_method\Mod.vdf",
    "upload_info_text": r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\scripts\python\upload_mod_to_workshop\upload_info.txt",
    "upload_dir": r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\upload_dir",
    "thumbnail_image": r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\Images\Testing.png",
    "kf_editor_ini": r"C:\Users\Mythical\Documents\My Games\KillingFloor2\KFGame\Config\KFEditor.ini",
    "ide_exe": "C:\\Users\\Mythical\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "icon_path": "C:\\Users\\Mythical\\Documents\\GitHub\\kf2_mythical\\kf2_modding_utility\\images\\kf2_icon_main.png"
}

with open('..\..\settings\settings.json', 'w') as file_2:
    json.dump(data_2, file_2, indent=4)
