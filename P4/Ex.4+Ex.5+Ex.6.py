import socket
import termcolor
from pathlib import Path

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080

# -- We define a function which returns a reading of a html doc. depending on the
# -- solicited page
def page_sorter(page):
    ret = ''
    if page == '/info/A':
        ret = Path('A.html').read_text()
    elif page == '/info/C':
        ret = Path('C.html').read_text()
    elif page == '/info/T':
        ret = Path('T.html').read_text()
    elif page == '/info/G':
        ret = Path('G.html').read_text()
    elif page == '/':
        ret = Path('index.html').read_text()
    else:
        ret = Path('error.html').read_text()
    return ret


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')
    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    request = req_line.split(' ')

    # This new contents are written in HTML language; We modify the <body> to print 'MODIFIED BY ME!!!'
    command = request[0]
    path = request[1]
    print(f'Command: {command}')
    termcolor.cprint(path, 'green')

    response = ''
    if command == 'GET':
        response = page_sorter(path)
        print(response)
    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(response)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + response
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()
