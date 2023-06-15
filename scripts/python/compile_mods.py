import subprocess

kf2_dir = r"C:\Program Files (x86)\Steam\steamapps\common\killingfloor2\Binaries\Win64"

subprocess.run(["kfeditor", "make"], cwd=kf2_dir)

quit()
