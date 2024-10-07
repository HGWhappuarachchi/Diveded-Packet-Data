
# File Transfer via Network (TCP/UDP)

This project demonstrates a simple client-server architecture for transferring a file from a client to a server over a network. The file is split into data packets of a specified size and sent either over TCP or UDP. The server reassembles the packets and saves the file on its end.

## Features

- **TCP Implementation**: Reliable file transfer using TCP connection.
- **UDP Implementation**: Unreliable but faster file transfer using UDP.
- **File Splitting**: File is split into packets (default 1024 bytes) before being sent.
- **Reassembling**: The server reassembles the packets into a complete file.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your machine.
- **Network Setup**: Both the client and server should be on the same network if you’re testing on different machines. If you’re running both locally, no additional setup is needed.

## Installation

1. Clone the repository (or copy the files) to your local machine.

    ```bash
    git clone https://github.com/your-username/file-transfer-tcp-udp.git
    cd file-transfer-tcp-udp
    ```

2. Ensure Python is installed by running:

    ```bash
    python --version
    ```

3. Install any necessary Python libraries (if applicable).

## Usage

### 1. Running the TCP Version

- **Step 1**: Start the server.

    In one terminal window, navigate to the project directory and run the server:

    ```bash
    python server.py
    ```

    This will start the server on `localhost` using port `65432`. The server will wait for incoming connections from the client.

- **Step 2**: Start the client.

    In another terminal window, navigate to the project directory and run the client:

    ```bash
    python client.py
    ```

    The client will connect to the server and send the contents of the file `file_to_send.txt` as packets. The server will receive the packets and reassemble the file, saving it as `received_file.txt`.

### 2. Running the UDP Version

- **Step 1**: Start the UDP server.

    In one terminal window, run the UDP server:

    ```bash
    python server_udp.py
    ```

    The server will listen for incoming UDP packets.

- **Step 2**: Start the UDP client.

    In another terminal window, run the UDP client:

    ```bash
    python client_udp.py
    ```

    The client will send the file `file_to_send.txt` as UDP packets. The server will reassemble the file and save it as `received_file_udp.txt`.

## Configuration

- **Port**: The default port used is `65432`. You can change this in both the client and server scripts.
- **Packet Size**: The default packet size is `1024` bytes (1KB). You can adjust this in the `split_data()` function in the client script.
  
## File Structure

```bash
.
├── README.md
├── client.py          # TCP client
├── client_udp.py      # UDP client
├── server.py          # TCP server
├── server_udp.py      # UDP server
├── file_to_send.txt   # Sample file to send (can be replaced with any file)
└── received_file.txt  # Received file on the server (TCP version)
└── received_file_udp.txt  # Received file on the server (UDP version)
```

## Notes

- **TCP vs. UDP**: TCP ensures all packets are received in the correct order but may be slower. UDP is faster but does not guarantee packet delivery or order.
- Ensure you use a different file for each transfer if testing both TCP and UDP simultaneously to avoid overwriting.
  
## Troubleshooting

- **Address Already in Use**: If you get this error when running the server, try changing the port number in both the server and client scripts to something different.
- **Connection Refused**: Make sure the server is running before starting the client. If running on different machines, ensure they are on the same network and firewall settings allow communication through the specified port.

