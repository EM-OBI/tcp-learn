# Initiate connection with server

import socket

# Server details that the client will connect to
HOST = "127.0.0.1"

PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST, PORT))


    # Data transfer

    #b indicates the data will be sent in 8-bit units
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data}")