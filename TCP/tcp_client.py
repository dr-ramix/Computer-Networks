import socket

def start_client(host, port):
    """
    Starts the TCP client.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to the server
        client.connect((host, port))
        print(f"[*] Connected to {host}:{port}")

        while True:
            message = input("Enter message to send (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break

            # Send data to the server
            client.sendall(message.encode('utf-8'))

            # Receive response from the server
            response = client.recv(1024)
            if not response:
                print("[*] Server disconnected.")
                break

            print(f"[*] Received from server: {response.decode('utf-8')}")

    except ConnectionRefusedError:
        print(f"[*] Connection refused. Make sure the server is running on {host}:{port}")
    except Exception as e:
        print(f"[*] An error occurred: {e}")
    finally:
        client.close()
        print("[*] Client connection closed.")

if __name__ == "__main__":
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 9999         # The port used by the server

    start_client(HOST, PORT)