import os
import json
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', 'settings', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

part_a = data["kf2_game_dir"]
part_b = "Binaries\WorkshopUserTool.exe"

workshop_user_tool_exe = f"{part_a}\{part_b}"
upload_info_text = data["upload_info_text"]

subprocess.run([workshop_user_tool_exe, upload_info_text])

quit()
