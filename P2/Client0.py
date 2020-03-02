# --- Easy class to message sending
import socket
from termcolor import colored

class Client:
    """A class for representing Clients"""

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f'Connection to SERVER at {self.ip}, PORT:{self.port}'

    @staticmethod
    def ping():
        print('OK!')

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode('utf-8')

        # Close the socket
        s.close()

        # Return the response
        return response

    def debug_talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        msg = colored(msg, 'blue')
        s.send(str.encode(msg))
        resp = s.recv(2048).decode('utf-8')
        response = colored(resp, 'green')
        s.close()
        return response

