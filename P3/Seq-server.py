import socket
from termcolor import colored
from Seq1 import Seq


def ping():
    response = f'OK!\n'
    print(response)
    return cs.send(str.encode(response))


def spl_in(in_msg):
    return in_msg.split(' ')[1]


def percentage(partial, tot):
    return round((partial*100)/tot, 1)


def get_seq(in_msg):
    index = int(spl_in(in_msg))
    response = dna_list[index]
    print(response)
    return cs.send(str.encode(response))


def info_seq(in_msg):
    get = Seq(spl_in(in_msg))
    f_msg = f'Sequence:{get}\n'
    len_seq = get.len()
    f_msg += f'Total length: {len_seq}\n'
    count_seq = get.count()
    for k, v in count_seq.items():
        perc = percentage(v, len_seq)
        codon = f'{k}: {v} ({perc}%)\n'
        f_msg += codon
    response = f_msg
    print(response)
    return cs.send(str.encode(response))


def comp_seq(in_msg):
    get = Seq(spl_in(in_msg))
    response = get.complement()
    print(response)
    return cs.send(str.encode(response))


def rev_seq(in_msg):
    get = Seq(spl_in(in_msg))
    response = get.reverse()
    print(response)
    return cs.send(str.encode(response))


def gene_file(in_msg):
    get = spl_in(in_msg)
    s0 = Seq()
    response = s0.read_fasta('/home/alumnos/gregocr/PycharmProjects/2019-2020-PNE-Practices/Session04/' + get)
    print(response)
    return cs.send(str.encode(response))


# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("SEQ server configured!")
nc = 0
client_ip_list = []
dna_list = ['ACTG', 'ACTGA', 'ACTGAC', 'ACTGACT', 'ACTGACTG']
doc_list = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
while True:
    if nc < 5:
        # -- Waits for a client to connect
        print("Waiting for Clients... ")

        try:
            (cs, client_ip_port) = ls.accept()

        # -- Server stopped manually
        except KeyboardInterrupt:
            print("Server stopped by the user")

            # -- Close the listenning socket
            ls.close()

            # -- Exit!
            exit()

        # -- Execute this part if there are no errors
        else:

            nc += 1
            client_ip_list.append(f'Client{nc}:{client_ip_port}')
            print("CONNECTION: {} From the IP: {}".format(nc, client_ip_port))

            # -- Read the message from the client
            # -- The received message is in raw bytes
            msg_raw = cs.recv(2048)

            # -- We decode it for converting it
            # -- into a human-redeable string
            msg = msg_raw.decode()

            if msg == 'PING':
                print(colored('PING command!', 'yellow'))
                ping()
                cs.close()
            elif 'GET' in msg:
                print(colored('GET command!', 'green'))
                get_seq(msg)
                cs.close()
            elif 'INFO' in msg:
                print(colored('INFO command!', 'blue'))
                info_seq(msg)
                cs.close()
            elif 'COMP' in msg:
                print(colored('COMP command!', 'magenta'))
                comp_seq(msg)
                cs.close()
            elif 'REV' in msg:
                doc = False
                for i in doc_list:
                    if i in msg:
                        doc = True
                if doc:
                    print(colored('GENE command!', 'white'))
                    gene_file(msg)
                    cs.close()
                else:
                    rev_seq(msg)
                    print(colored('REV command!', 'cyan'))
                    cs.close()

    else:
        print(f'The following clients have sended a message to the server:')
        for i in client_ip_list:
            print(i)
        ls.close()
        exit()
