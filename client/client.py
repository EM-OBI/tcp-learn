import socket
import threading

# Define ports and server
PORT = 5050
SERVER = "192.168.0.135"
ADDR = (SERVER, PORT)
# Create header that is 64 bytes and will tell us the size of incoming date
HEADER = 64

FORMAT = "utf-8"

DISCONNECT_MESSAGE = "bye"

# create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))

    #send message
    client.send(send_length)
    client.send(message)

def receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            print(msg)
        except:
            print("Disconnected from server")
            break

#receiver thread
threading.Thread(target=receive, daemon=True).start()

# Chat loop
while True:
    msg = input("> ")

    if msg.lower() == DISCONNECT_MESSAGE:
        send(msg)
        break

    send(msg)




