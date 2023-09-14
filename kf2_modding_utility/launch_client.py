import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NEW_SCRIPT_DIR = f"{SCRIPT_DIR}/client/scripts/python"

os.chdir(NEW_SCRIPT_DIR)

subprocess.Popen("python main.py")

sys.exit()
