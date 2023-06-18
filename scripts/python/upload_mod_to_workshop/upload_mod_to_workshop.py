import json
import subprocess

settings_json = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\other\settings.json"

with open(settings_json) as file:
    data = json.load(file)

part_a = data["kf2_game_dir"]
part_b = "Binaries\WorkshopUserTool.exe"

workshop_user_tool_exe = f"{part_a}\{part_b}"
upload_info_text = data["upload_info_text"]

subprocess.run([workshop_user_tool_exe, upload_info_text])

quit()
