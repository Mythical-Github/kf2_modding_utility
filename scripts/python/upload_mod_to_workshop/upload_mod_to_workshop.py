import subprocess


workshop_user_tool_exe = "C:/Program Files (x86)/Steam/steamapps/common/killingfloor2/Binaries/WorkshopUserTool.exe"
upload_info_text = "upload_info.txt"


subprocess.run(f"{workshop_user_tool_exe} {upload_info_text}")


quit()
