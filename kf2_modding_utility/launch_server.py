import os
import json
import subprocess


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_JSON = os.path.normpath(os.path.join(SCRIPT_DIR, "kf2_modding_utility_client/settings/settings.json"))


with open(SETTINGS_JSON) as settings_json:
    settings_data = json.load(settings_json)

script_path = os.path.join(SCRIPT_DIR, "kf2_modding_utility_server/scripts/python/main.py")


def main():
    if settings_data["show_log_window"] == "true":
        subprocess.Popen(["python", script_path])
    else:
        subprocess.Popen(["pythonw", script_path])


if __name__ == "__main__":
    main()
