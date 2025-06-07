import socket
import threading

def handle_client(client_socket, addr):

    print(f"Accepted connection from {addr[0]}:{addr[1]}")

    try: 
        while True:
            #receive data from the client
            data = client_socket.recv(1024) # 1024 bytes for buffer size
            if not data: 
                print(f"Connection closed by {addr[0]}:{addr[1]}")
                break # if no data is received, the connection is closed

            message = data.decode('utf-8')
            print(f"Received from {addr[0]}:{addr[1]}: {message}")

            # Echo the message back to the client
            client_socket.sendall(data)

    except Exception as e:
        print(f"Error handling client {addr[0]}:{addr[1]}: {e}")

    finally:
        client_socket.close()
        print(f"Connection with {addr[0]}:{addr[1]} closed.")

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)  # Allow up to 5 connections in the queue
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            client_socket, addr = server.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Localhost
    PORT = 9999       # Port to listen on (non-privileged ports are > 1023)
    start_server(HOST, PORT)
    print(f"Server started on {HOST}:{PORT}")
#Hello