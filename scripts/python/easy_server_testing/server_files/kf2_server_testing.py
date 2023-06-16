import socket

# Host and port to listen on
host = ""
port = 

# Command to run on the VPS
command_to_run = r"C:\Users\Administrator\Desktop\kf2_server_restarter.py"

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(host, port))

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    
    # Receive the command from the client
    received_command = client_socket.recv(1024).decode()
    print('Received command:', received_command)
    
    if received_command == 'run_command':
        # Execute the command on the VPS
        import subprocess
        subprocess.call(command_to_run, shell=True)
    
    # Close the client connection
    client_socket.close()
