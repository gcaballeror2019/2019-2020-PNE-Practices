from Client0 import Client


# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print("Sending a message to the server...")
response = c.talk("REV ACTGTGTGTGTGTGTACTGATG")
print(response)