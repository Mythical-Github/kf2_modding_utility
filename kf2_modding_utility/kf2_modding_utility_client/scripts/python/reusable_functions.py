import os
import sys
import webbrowser
from pathlib import Path


def kill_task(task):
    os.system(f"taskkill /f /im {task}.exe")


def open_dir_in_file_browser(dir_path):
    if Path(dir_path).is_dir():
        if sys.platform.startswith('win'):
            os.startfile(dir_path)
        elif sys.platform.startswith('linux'):
            os.system(f'xdg-open "{dir_path}"')
        else:
            print("Unsupported platform.")
    else:
        print("Directory path is invalid or doesn't exist.")


def open_website(url):
    webbrowser.open(url)
    pass
