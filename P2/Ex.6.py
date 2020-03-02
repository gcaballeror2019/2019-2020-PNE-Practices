from Client0 import Client
from pathlib import Path


def div_seq(filename):
    dna_str = ''
    file = Path(filename).read_text()
    lines = file.split('\n')
    string = lines[1:]
    dna_str = dna_str.join(string).replace(',', '')
    spl_str = []
    n = 10
    for index in range(0, len(dna_str), n):
        spl_str.append(dna_str[index: index + n])
    return dna_str, spl_str


PRACTICE = 2
EXERCISE = 6

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
response1 = f'NULL seq created'
response2 = div_seq(filename)[0]
response_list = [response1, response2]
print(f'{c.debug_talk(dna_string)}')
for i in div_seq(filename)[1]:
    print(f'To server:  {i} \n From server:  {c.debug_talk(i)}')
    if div_seq(filename)[1].index(i) > 3:
        break