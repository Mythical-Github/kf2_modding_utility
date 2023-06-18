import json

data = {
    "kf2_server_ip": "23.105.148.17",
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
    "thumbnail_image": r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\scripts\python\upload_mod_to_workshop_alt_method\Testing.png",
    "kf_editor_ini": r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\inis\KFEditor.ini"
}

with open('settings.json', 'w') as file:
    json.dump(data, file, indent=4)
