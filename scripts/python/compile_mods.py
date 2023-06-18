import os
import subprocess

kf2_dir = r""

os.chdir(kf2_dir)

subprocess.run(["kfeditor.exe", "make"])

quit()
