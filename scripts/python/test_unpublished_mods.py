import subprocess

steam_exe = r"C:\Program Files (x86)\Steam\steam.exe"
package_name = "Mythical"
game_mode = "KFGameInfo_Mythical"
map_name = "KF-ZedsDiner"
mutator_name = "KF_Mutator_Mythical"
steam_app_id = 232090

command = [
    steam_exe,
    "-applaunch",
    str(steam_app_id),
    f"{map_name}?game={package_name}.{game_mode}?mutator={package_name}.{mutator_name},ServerExtMut.ServerExtMut",
    "-log",
    "-useunpublished"
]

subprocess.run(command)

quit()
