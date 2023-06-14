import os


package_name = r"Mythical"
game_mode = r"KFGameInfo_Mythical"
map_name = r"KF-ZedsDiner"
mutator_name = r"KF_Mutator_Mythical"
kf2_dir = r"C:\Program Files (x86)\Steam\steamapps\common\killingfloor2\Binaries\Win64"


os.chdir(kf2_dir)
os.system(f"KFGame.exe {map_name}?game={package_name}.{game_mode}?mutator={package_name}.{mutator_name} -log -useunpublished")


quit()
