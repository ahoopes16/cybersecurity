import socket
from client import Client

"""
Dedicated server listening for a connection from any of the machines 
trying to break DES. Once it receives a connection from any of them, 
it will send a connection to the terminal servers on the other machines 
to terminate them.
@authors Adam Callanan, Sage Elfanbaum, Kevin Hoopes, Dustin Roan, Jeremy Schmich
@version 10/30/2017
"""

# List of all machines' IP addresses for termination
computers = ['150.243.146.253']

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = socket.gethostname()
port = 10001
print('starting up on localhost port ' + str(port))
sock.bind((server_address, port))

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('Terminate Order from: ', client_address)
        for pc in computers:
            Client(pc, 10000).main()

    finally:
        # Clean up the connection
        connection.close()
