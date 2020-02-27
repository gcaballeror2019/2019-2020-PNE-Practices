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
