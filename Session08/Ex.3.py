import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.253.169"

while True:
    # --- Ask the user for the message
    message = input('Write the message to send')
    # --- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # --- Establish the connection to the Server
    s.connect((IP, PORT))
    # --- Send the user message
    s.send(str.encode(message))

    msg_raw = s.recv(2048)
    msg = msg_raw.decode()
    print(f"Message received: {msg}")
    # --- Close the socket
    s.close()
