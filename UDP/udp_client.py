import socket
import time

TARGET_IP = "127.0.0.1" #local IP-address
TARGET_PORT = 55555 #port to send data to

NUM_MESSAGES = 1000

# Create a UDP socket
#(AF_INET for IPv4, SOCK_DGRAM for UDP)
#AF = Address Family
client_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"UDP client started, sending {NUM_MESSAGES} messages to {TARGET_IP}:{TARGET_PORT} | Target IP: {TARGET_IP} | Target Port: {TARGET_PORT}")

sent_messages_counter = 0

try:
    for i in range(1, NUM_MESSAGES + 1):
        message = f"Message {i}"

        client_udp_socket.sendto(message.encode(), (TARGET_IP, TARGET_PORT))
        sent_messages_counter += 1

        time.sleep(0.001)  # Sleep for 1 milliseconds to avoid flooding
        # Print progress every 100 messages
        if  i % 100 == 0:
            print(f"Sent {i} messages so far...")

    print(f"\"All {sent_messages_counter} messages sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    client_udp_socket.close()
    print("UDP client socket closed.")