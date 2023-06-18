import os
import socket
import subprocess

content_brewer_py = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\scripts\python\brew_kf2_mods.py"
workshup_uploader_py = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\scripts\python\upload_mod_to_workshop_alt_method\upload_mod_to_workshop_alt_method.py"
open_kf2_to_server_py = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\scripts\python\open_kf2_to_server.py"

# Host and port of the VPS
host = ""
port = 0

# subprocess.run(["python", content_brewer_py])

subprocess.run(["python", workshup_uploader_py])

# Command to send to the VPS
command_to_send = 'run_command'

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send the command to the server
client_socket.sendall(command_to_send.encode())

# Close the connection
client_socket.close()

os.system("taskkill /f /im steam.exe")

subprocess.Popen(["python", open_kf2_to_server_py])