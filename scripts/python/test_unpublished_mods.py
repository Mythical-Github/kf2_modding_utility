import subprocess

steam_exe = r""
package_name = ""
game_mode = ""
map_name = ""
mutator_name = ""
steam_app_id = 0

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
