import http.server
import socketserver
import termcolor
from pathlib import Path


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analyze the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # It contains the resource name without the / symbol
        # If this string is blank "", it means the main page
        path = path[1:]

        # -- Content type header
        # -- Both, the error and the main page are in plain text in this examples
        content_type = 'text/html'

        # -- Gives a response depending of the existence of de
        if path == "":
            termcolor.cprint("Main page req", 'green')
            # Message to send back to the client
            contents = Path('index.html').read_text()
            # Status code is ok
            status = 200

        elif path == "info/A":
            termcolor.cprint("A info page req", 'green')
            # Message to send back to the client
            contents = Path('A.html').read_text()
            # Status code is ok
            status = 200

        elif path == "info/C":
            termcolor.cprint("C info page req", 'green')
            # Message to send back to the client
            contents = Path('C.html').read_text()
            # Status code is ok
            status = 200

        elif path == "info/T":
            termcolor.cprint("T info page req", 'green')
            # Message to send back to the client
            contents = Path('T.html').read_text()
            # Status code is ok
            status = 200

        elif path == "info/G":
            termcolor.cprint("G info page req", 'green')
            # Message to send back to the client
            contents = Path('G.html').read_text()
            # Status code is ok
            status = 200
        else:
            # -- not found
            termcolor.cprint("ERROR: Not found", 'red')

            # Message to send back to the client
            contents = Path('Error.html').read_text()

            # Status code is NOT FOUND
            status = 404

        # Generating the response message
        self.send_response(status)

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()