import socket
import sys

computers = []
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = socket.gethostname()
port = 10000
print('starting up on localhost port ' + str(port))
sock.bind((server_address, port))

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        sys.exit(0)

    finally:
        # Clean up the connection
        connection.close()

