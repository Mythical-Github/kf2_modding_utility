import os
import socket

host = "127.0.0.1"
port = 1234

game_dir = r"C:\game_servers\killing_floor_2"
task_name = "KFServer.exe"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print('Server is listening on {}:{}'.format(host, port))

def start_server():
    return

def restart_server():
    close_server()
    start_server()

def close_server():
    os.system(f"taskkill /f /im {task_name}")

def update_server():
    close_server()

    start_server()

def add_new_workshop_to_server_subscriptions():
    close_server()

    start_server()

while True:

    client_socket, client_address = server_socket.accept()
    received_command = client_socket.recv(1024).decode()
    print('Received command:', received_command)
    
    if received_command == 'restart_server':
        print('restart_server')
        restart_server()

    if received_command == 'update_server':
        print('update_server')
        update_server()

    if received_command == 'close_server':
        print('close_server')
        close_server()

    if received_command == 'start_server':
        print('start_server')
        start_server()
                        
    if received_command.startswith('add_new_workshop_to_subscriptions'):
        print('add_new_workshop_to_subscriptions')
        add_new_workshop_to_server_subscriptions()

    client_socket.close()
