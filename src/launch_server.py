import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NEW_SCRIPT_DIR = f"{SCRIPT_DIR}/kf2_modding_utility_server"

os.chdir(NEW_SCRIPT_DIR)

subprocess.Popen("python main.py")

sys.exit()
