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
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.153"
PORT = 8080
PORT2 = 8081

# -- Create a client object
c = Client(IP, PORT)
c2 = Client(IP, PORT2)
filename = 'C:/Users/Usuario/PycharmProjects/2019-2020-PNE-Practices2/Session04/U5.txt'
EV_lst = []
OD_lst = []
for i in div_seq(filename)[1]:
    if div_seq(filename)[1].index(i) % 2 == 0:
        EV_lst.append(i)
    else:
        OD_lst.append(i)
file_contents = Path(filename).read_text()
dna_string = file_contents.split('\n', 1)
dna_string = dna_string[1].replace('\n', '')

print('Sending a message to the server...')
response1 = f'NULL seq created'
print('From server: ', c.debug_talk(response1))
print("From server: ", c2.debug_talk(response1))
for i in EV_lst:
    print(f'From server:  {c.debug_talk(i)} ')
    if EV_lst.index(i) == 4:
        break
for i in OD_lst:
    print(f'From server:  {c2.debug_talk(i)} ')
    if OD_lst.index(i) == 4:
        break