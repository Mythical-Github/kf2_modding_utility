import os
import subprocess

kf2_dir = r"C:\Program Files (x86)\Steam\steamapps\common\killingfloor2\Binaries\Win64"

os.chdir(kf2_dir)

subprocess.run(["kfeditor.exe", "make"])

quit()
