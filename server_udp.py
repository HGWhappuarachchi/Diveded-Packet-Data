# server_udp.py
import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
server_socket.bind(server_address)

print("Waiting for UDP packets...")

received_data = b""
while True:
    data, address = server_socket.recvfrom(1024)  # Receive in 1 KB chunks
    if not data:
        break
    received_data += data

# Save the received data to a file
with open('received_file_udp.txt', 'wb') as f:
    f.write(received_data)

print("File received and saved as 'received_file_udp.txt'.")
