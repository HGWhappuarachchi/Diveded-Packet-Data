# server.py
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for a connection...")

# Accept connection
connection, client_address = server_socket.accept()
try:
    print(f"Connection from {client_address}")

    # Receive the data in small chunks and reassemble it
    received_data = b""
    while True:
        data = connection.recv(1024)  # Receive in 1 KB chunks
        if not data:
            break
        received_data += data

    # Save the received data to a file
    with open('received_file.txt', 'wb') as f:
        f.write(received_data)
    print("File received and saved as 'received_file.txt'.")

finally:
    connection.close()
