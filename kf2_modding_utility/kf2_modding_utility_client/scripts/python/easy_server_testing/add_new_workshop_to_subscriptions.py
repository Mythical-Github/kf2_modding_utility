import os
import json
import socket

script_dir = os.path.dirname(os.path.abspath(__file__))
settings_json = os.path.join(script_dir, '..', '..', '..', 'settings', 'settings.json')

with open(settings_json) as file:
    data = json.load(file)

host = data["kf2_server_ip"]
port = data["easy_testing_port"]

command_to_send = "add_new_workshop_to_subscriptions"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

client_socket.sendall(command_to_send.encode())

client_socket.close()