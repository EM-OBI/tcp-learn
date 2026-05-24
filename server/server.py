import socket
import threading

# Define ports and server
PORT = 5050

SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

# Create header that is 64 bytes and will tell us the size of incoming date
HEADER = 64

FORMAT = "utf-8"

DISCONNECT_MESSAGE = "!DISCONNECTED"

# Define socket (family, type)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address
server.bind(ADDR)


#create list of messages
# msg = 


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected: 
        # This is blocking and waits to receive message from client
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    
    conn.close()


# Start server and listen for new connections
def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        # Use blocking
        conn, addr = server.accept()

        # Thread
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        # Show us the number of threads running i.e. all the connections
        print(f"ACTIVE CONNECTIONS {threading.active_count() - 1}")



# Call start
print(f"Server is starting...")
start()