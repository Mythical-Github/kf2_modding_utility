import subprocess

settings_json = r"..\other\settings.json"

subprocess.run(['start', '', settings_json], shell=True)

quit()
