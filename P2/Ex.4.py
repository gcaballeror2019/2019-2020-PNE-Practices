from Client0 import Client


PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.153"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print('Sending a message to the server...')
response1 = 'Message 1:...'
response2 = 'Message 2: Testing!!!'
response_list = [response1, response2]
for i in response_list:
    print(f'To server:  {i} \n From server:  {c.debug_talk(i)}')