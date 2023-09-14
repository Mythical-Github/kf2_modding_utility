import sys
import subprocess
from main import SETTINGS_JSON


subprocess.Popen(['start', '', SETTINGS_JSON], shell=True)


sys.exit()
