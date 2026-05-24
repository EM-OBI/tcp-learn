import socket

# Define ports and server
PORT = 5050
SERVER = "192.168.0.135"
ADDR = (SERVER, PORT)
# Create header that is 64 bytes and will tell us the size of incoming date
HEADER = 64

FORMAT = "utf-8"

DISCONNECT_MESSAGE = "!DISCONNECT"

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

    #print received message
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Michael!")

send(DISCONNECT_MESSAGE)

