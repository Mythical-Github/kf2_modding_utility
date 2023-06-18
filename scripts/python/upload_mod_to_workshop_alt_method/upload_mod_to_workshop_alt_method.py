import subprocess

username = ""
password = ""
steam_cmd_exe = r""
mod_vdf = r""

subprocess.run(f"{steam_cmd_exe} +login {username} {password} +workshop_build_item {mod_vdf} +quit")