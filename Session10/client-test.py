from Client0 import Client
from termcolor import colored
PORT = 8081
IP = "212.128.253.169"

s = Client(IP, PORT)

for i in range(5):
    print('To Server:', colored(f'Message {i+1}', 'blue'))
    print(f'From Server:', s.debug_talk(colored(f'Message {i+1}', 'green')))
