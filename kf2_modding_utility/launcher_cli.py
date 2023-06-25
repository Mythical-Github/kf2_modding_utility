import sys
import time
from kf2_modding_utility_client import kf2_modding_utility_client
from kf2_modding_utility_server import kf2_modding_utility_server


def main():
    if len(sys.argv) > 1:
        app_choice = sys.argv[1].lower()
        if app_choice == "client":
            kf2_modding_utility_client.main()
        elif app_choice == "server":
            kf2_modding_utility_server.main()
        else:
            print("Invalid app choice.")
    else:
        print("Please specify the app choice as a command-line argument (client/server).")


if __name__ == "__main__":
    main()
