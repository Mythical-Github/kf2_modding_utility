import os
import sys
import json
import socket
from main import SETTINGS_JSON


with open(SETTINGS_JSON) as file:
    DATA = json.load(file)


HOST = DATA["kf2_server_ip"]
PORT = DATA["easy_testing_PORT"]


COMMAND_TO_SEND = "start_server"


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((HOST, PORT))


client_socket.sendall(COMMAND_TO_SEND.encode())


client_socket.close()

sys.exit()
