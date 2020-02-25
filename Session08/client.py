import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8080
IP = "192.168.124.179"


# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Closing the socket
s.close()