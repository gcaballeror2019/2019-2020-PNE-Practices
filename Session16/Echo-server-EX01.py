from pathlib import Path
import http.server
import termcolor
import socketserver

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

        # -- Print the request line
        termcolor.cprint(self.requestline, 'green')

        # -- Analyze the request line
        req_line = self.requestline.split(' ')

        # -- Get the path. It always start with the / symbol
        path = req_line[1]

        # --  Check all the arguments
        arguments = path.split('?')

        # -- The verb is located as the first argument
        verb = arguments[0]

        status = 404
        contents = Path('Error.html').read_text()
        # -- Gives a response depending of the existence of de
        if verb == '/':
            # OPen form-1 file (HTML)
            contents = Path('form-EX01.html').read_text()
            # Status code
            status = 200
        elif verb == '/echo':
            # -- Get the sub-argument next to ?
            sub_a = arguments[1]
            name, value = sub_a.split('=')
            contents = '''
                        <!DOCTYPE html>
                        <html lang='en'>
                        <head>
                            <meta charset='utf-8'>
                            <title>Echo</title>
                        </head>
                        <body>
                        <h2>Received message:</h2>
                        '''
            contents += f'<p>{value}</p>'
            contents += '<a href="/">Main page</a>'
            contents += '</body></html>'
            status = 200

        # -- Generating the response message
        self.send_response(status)

        # -- Define the content-type header:
        content_type = 'text/html'
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # -- The header is finished
        self.end_headers()

        # -- Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client; Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('')
        print('Stopped by the user')
        httpd.server_close()
