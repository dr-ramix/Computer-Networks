import socket
import time
import random


HOST_IP = "127.0.0.1"  # Local IP address for the server
HOST_PORT = 55555      # Port to listen for incoming data
BUFFER_SIZE = 1024     # Size of the buffer to receive data


#global counter
received_messages_counter = 0
dropped_messages_counter = 0

# Create a UDP socket (AF_INET for IPv4, SOCK_DGRAM for UDP) -> (IPv4, UDP), INET = IP
server_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Bind the socket to the address and port
    server_udp_socket.bind((HOST_IP, HOST_PORT))
    print(f"UDP SERVER started, listening on {HOST_IP}:{HOST_PORT}")
    print("Simulating packet loss...")
    print("Waiting for incoming messages...")


    while True:
        # Receive data from the client, maximum BUFFER_SIZE bytes at a time
        data, addr = server_udp_socket.recvfrom(BUFFER_SIZE)
        received_message = data.decode('utf-8')

        #simulate packet loss, in the local network, there is no packet loss, so we simulate it.
        if random.randint(1, 10) > 7: # 30% Chance that it drops the packet
            dropped_messages_counter += 1
            print(f"Packet of '{received_message}' from {addr} dropped (Total dropped: {dropped_messages_counter})")
            continue  # Skip to the next iteration without processing the packet


        time.sleep(0.01)

        received_messages_counter += 1
        print(f"received by {addr}: '{received_message}' (Total received: {received_messages_counter})")


except KeyboardInterrupt:
    print("\nUDP server stopped by user.")
    print(f"Total received messages: {received_messages_counter}, Total dropped messages: {dropped_messages_counter}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server_udp_socket.close()
    print("UDP server socket closed.")
    print("Exiting UDP server.")