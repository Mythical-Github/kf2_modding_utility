import subprocess

package_name = r"Mythical"
kf2_dir = r"C:\Program Files (x86)\Steam\steamapps\common\killingfloor2\Binaries\Win64"

subprocess.run(["kfeditor", f"brewcontent -platform=PC {package_name}"], cwd=kf2_dir)

quit()
