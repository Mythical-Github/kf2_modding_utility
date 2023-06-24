import subprocess
import sys
from pathlib import Path

dir_path = Path(__file__).resolve().parent.parent.parent

if Path(dir_path).is_dir():
    if sys.platform.startswith('win'):
        subprocess.run(['explorer', dir_path], shell=True)
    elif sys.platform.startswith('linux'):
        subprocess.run(['xdg-open', dir_path])
    else:
        print("Unsupported platform.")
else:
    print("Directory path is invalid or doesn't exist.")
