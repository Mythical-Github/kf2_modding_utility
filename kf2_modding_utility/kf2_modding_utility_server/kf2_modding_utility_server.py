import os
import sys
import subprocess

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

py_to_run = f"{script_directory}\scripts\python\main.py"

subprocess.Popen(["python", py_to_run])

quit()
