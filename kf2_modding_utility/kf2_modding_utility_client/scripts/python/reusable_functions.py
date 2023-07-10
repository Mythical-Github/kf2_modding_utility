import os
import sys


def kill_task(task):
    os.system(f"taskkill /f /im {task}.exe")
    

sys.exit()
