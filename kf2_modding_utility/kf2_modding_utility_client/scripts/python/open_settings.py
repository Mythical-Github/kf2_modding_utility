import sys
import subprocess

settings_json = r"..\..\settings\settings.json"

subprocess.Popen(['start', '', settings_json], shell=True)

sys.exit()
