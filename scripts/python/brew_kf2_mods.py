import os

package_name = r""
kf2_dir = r""

os.chdir(kf2_dir)
os.system(f"kfeditor brewcontent -platform=PC {package_name}")

quit()
