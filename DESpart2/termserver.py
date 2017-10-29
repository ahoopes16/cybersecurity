import socket
import crackclient
import sys

computers = []
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('Terminate Order from: ', client_address)
        for pc in computers:
            crackclient(pc, 10000)

    finally:
        # Clean up the connection
        connection.close()

