# client_udp.py
import socket

# Function to split data into smaller chunks (packets)
def split_data(data, chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 65432)

# Open the file to be sent and split it into packets
file_name = 'file_to_send.txt'  # Ensure this file exists in the same directory
with open(file_name, 'rb') as file:
    file_data = file.read()

packets = split_data(file_data, 1024)  # Split file into 1 KB packets

# Send each packet to the server
for packet in packets:
    client_socket.sendto(packet, server_address)

print("File sent successfully over UDP!")
client_socket.close()
