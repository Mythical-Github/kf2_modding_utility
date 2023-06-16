import subprocess

username = ""
password = "
steam_cmd_exe = r"C:\Programs\steamcmd\steamcmd.exe"
mod_vdf = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\scripts\python\upload_mod_to_workshop_alt_method\Mod.vdf"

subprocess.run(f"{steam_cmd_exe} +login {username} {password} +workshop_build_item {mod_vdf} +quit")