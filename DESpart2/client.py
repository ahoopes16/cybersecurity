import socket


class Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port

    def main(self):
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

        finally:
            print('closing socket')
            sock.close()


# Client('150.243.200.174', 10000).main()
