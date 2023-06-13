import os

package_name = r"Mythical"
kf2_dir = r"C:\Program Files (x86)\Steam\steamapps\common\killingfloor2\Binaries\Win64"

os.chdir(kf2_dir)
os.system(f"kfeditor brewcontent -platform=PC {package_name}")

quit()
