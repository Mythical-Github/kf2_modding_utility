import json
import subprocess
from pathlib import Path

settings_json = Path(__file__).resolve().parent.parent.parent / 'settings' / 'settings.json'

with open(settings_json) as file:
    data = json.load(file)

part_a = data["kf2_game_dir"]
part_b = "Binaries\WorkshopUserTool.exe"

workshop_user_tool_exe = f"{part_a}\{part_b}"
upload_info_text = data["upload_info_text"]

subprocess.Popen([workshop_user_tool_exe, upload_info_text])

quit()
