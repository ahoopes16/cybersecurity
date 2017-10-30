import socket

"""
Class to implement a TCP network client. Sends a connection to the 
ded_server when the key is found on the current machine.
@authors Adam Callanan, Sage Elfanbaum, Kevin Hoopes, Dustin Roan, Jeremy Schmich
@version 10/30/2017
"""


class Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port

    def main(self):
        """
        Main Program
        Send a quick connection to the ded_server to let it know
        the key was found and it should tell the other machines to
        terminate
        """
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.server_address, self.server_port)
        print('connecting to ' + self.server_address + ' on port ' + str(self.server_port))
        sock.connect(server_address)

        try:
            # Send data
            message = b'TERMINATE!!!'
            print('EXTERMINATE EXTERMINATE EXTERMINATE')
            sock.sendall(message)
        # Close the socket
        finally:
            print('closing socket')
            sock.close()
