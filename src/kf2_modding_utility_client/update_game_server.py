import sys
import json
import socket
from main import CLIENT_SETTINGS_JSON


with open(CLIENT_SETTINGS_JSON) as file:
    data = json.load(file)


host = data["kf2_server_ip"]
port = data["easy_testing_port"]


command_to_send = "update_server"


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((host, port))


client_socket.sendall(command_to_send.encode())


client_socket.close()


sys.exit()
