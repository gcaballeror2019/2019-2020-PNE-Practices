from Seq1 import Seq
from pathlib import Path
import http.server
import termcolor
import socketserver
import json
import http.client


# Server's Port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# -- Server used for the project
server = 'rest.esembl.org'
params = '?content-type=application/json'

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

        contents = Path('Error.html').read_text()
        status = 404

        # -- Gives as response the index.html if there is no requested action
        try:
            if verb == '/':
                contents = Path('index.html').read_text()

            elif verb == '/listSpecies':
                contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                 <meta charset = "utf-8" >
                                 <title>List of species in the browser</title >
                                </head >
                                <body>
                                <p>The total number of species in ensembl is: 267</p>"""
                pair = arguments[1]
                s_name = pair.split('?')
                name, i = s_name[0].split('=')
                contents += f"""<{i}>"""
                end_p = 'info/species'
                connect = http.client.HTTPConnection(server)
                req = end_p + params

                try:
                    connect.request('GET', req)
                except ConnectionRefusedError:
                    print('An error has occurred, Can´t connect to the server')
                    exit()
                resp = connect.getresponse()
                main_b = resp.read().decode()
                lim_l = []
                main_b = json.loads(main_b)
                lim = main_b['species']
                if i > len(lim):
                    contents = f"""<!DOCTYPE html>
                            <html lang = "en">
                            <head>
                             <meta charset = "utf-8" >
                             <title>error</title >
                            </head>
                            <body>
                            <p>ERROR Limit not found. Introduce a valid value</p>
                            <a href="/">Main page</a></body></html>"""
                else:
                    for e in lim:
                        lim_l.append(e['display_name'])
                        if len(lim_l) == i:
                            contents += f"""<p>The species are:</p>"""
                            for s in lim_l:
                                contents += f"""<p> - {s}</p>"""
                    contents += f"""<a href='/'> [Main page] </a></body></html>"""
        except (KeyError, ValueError, IndexError, TypeError):
            contents = Path('error.html').read_text()
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

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('')
        print('Stopped by the user')
        httpd.server_close()