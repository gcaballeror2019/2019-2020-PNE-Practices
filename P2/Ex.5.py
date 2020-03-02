from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.153"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
filename = 'C:/Users/Usuario/PycharmProjects/2019-2020-PNE-Practices2/Session04/U5.txt'
file_contents = Path(filename).read_text()
dna_string = file_contents.split('\n', 1)
dna_string = dna_string[1].replace('\n', '')

print('Sending a message to the server...')
response1 = f'Sending gene {filename}'
response2 = dna_string
response_list = [response1, response2]
for i in response_list:
    print(f'To server:  {i} \n From server:  {c.debug_talk(i)}')