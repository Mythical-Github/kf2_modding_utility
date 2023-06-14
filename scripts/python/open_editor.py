import subprocess


steam_exe = "C:\Program Files (x86)\Steam\steam.exe"
steam_app_id = 232150


subprocess.run(f"{steam_exe} -applaunch {steam_app_id} -NoGADWarning")


quit()
