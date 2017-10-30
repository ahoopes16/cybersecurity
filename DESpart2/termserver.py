import socket

"""
Terminal server to be attached to each machine's main program.
Sits and waits for a connection from the ded_server. Once received, 
terminates the program.
@authors Adam Callanan, Sage Elfanbaum, Kevin Hoopes, Dustin Roan, Jeremy Schmich
@version 10/30/2017
"""


def create_server():
    """
    Create a terminal server and wait for a connection from
    the dedicated server.
    :return: True when a connection is received
    """
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
            # Tell program to terminate
            print("Key Found... Term Server Terminating DES Key Search")
            return True
        finally:
            # Clean up the connection
            connection.close()
