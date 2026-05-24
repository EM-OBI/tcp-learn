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

# Create list to handle all connected clients
Clients = []

#create list of messages
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    Clients.append(conn)

    connected = True
    while connected: 
        # This is blocking and waits to receive message from client
        try: 
            msg_length = conn.recv(HEADER).decode(FORMAT)

            if msg_length: 
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)

                if msg == DISCONNECT_MESSAGE:
                    connected = False

                #Call broadcast
                broadcast(conn, addr, msg)
                # print(f"[{addr}] {msg}")
            
            else: 
                break
        
        except (ConnectionResetError, ConnectionAbortedError):

            print(f"[DISCONNECT] {addr} lost connection unexpectedly")

            break

        except Exception as e:

            print(f"[ERROR] {addr}: {e}")

            break
            
    # cleanup
    if conn in Clients:
        Clients.remove(conn)

    conn.close()
    print(f"[CLOSED] {addr}")

# Start server and listen for new connections
def start():
    server.listen(3)
    print(f"Server is listening on {SERVER}")
    while True:
        # Use blocking
        conn, addr = server.accept()

        # Thread
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        # Show us the number of threads running i.e. all the connections
        print(f"ACTIVE CONNECTIONS {threading.active_count() - 1}")

# Create broadcast functionality
def broadcast(sender_conn, sender_addr, msg):
    message = f"[{sender_addr}] {msg}".encode(FORMAT)

    for client in Clients: 
        if client != sender_conn:
            client.send(message)

    


# Call start
print(f"Server is starting...")
start()