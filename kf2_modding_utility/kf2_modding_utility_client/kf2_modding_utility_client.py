import os
import sys
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

os.system("python scripts/python/main.py")

sys.exit()
