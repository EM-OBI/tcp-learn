# import socket module

import socket

# set up listening socket

HOST = "127.0.0.1"

PORT = 5050

# create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind newly created socket to host and port you want to listen to
    s.bind((HOST, PORT))

    # Listen
    s.listen()
    print(f"server is listening")
    # Use blocking to prevent program from running until incoming request is accepted
    conn, addr = s.accept()

# Data exchange in echo server
with conn:
    print (f"Connected by {addr}")

    # Start loop and continue as long as client is sending data
    while True: 
        data = conn.recv(1024)
        # End loop if no data is sent
        if not data:
            break
        # If data is sent, then send exact data back to client
        conn.sendall(data)

