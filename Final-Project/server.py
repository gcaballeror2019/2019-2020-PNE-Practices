import http.server
import socketserver
import termcolor
from pathlib import Path
import json


# -- Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# -- Def. the list of seq. for GET option:
SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]


# -- Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# -- It means that our class inherits all his methods and properties

class TestHandler(http.server.BaseHTTPRequestHandler):
    global contents

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        server = "rest.ensembl.org"
        params = "?content-type=application/json"

        # -- Print req_line
        termcolor.cprint(self.requestline, 'green')

        # -- Analyze the req_line:
        req_line = self.requestline.split(' ')

        # -- Get the path that starts with "/"
        path = req_line[1]

        # -- Read the arguments
        arguments = path.split('?')

        # -- Get the order asked
        action = arguments[0]

        # -- Def. the contents and the status:
        contents = Path('Error.html').read_text()
        status = 200

        try:

            # -- Main page (index):
            if action == "/":
                contents = Path('index.html').read_text()

            # _______ Basic Lv. _______

            # -- List Species: List the names of all the species available in the database. Might be limited by the user
            # by entering a limit

            elif "/listSpecies" in action:

                # -- We extract the input limit nº:
                lim = arguments[1]

                # -- This endpoint lists:  -All available species  -Aliases  -Available adaptor groups  -Data release.
                end_p = "info/species"

                try:

                    # Connect with the server
                    connect = http.client.HTTPConnection(server)

                    # -- Send the request message, using the GET method. The main page is requested
                    try:
                        connect.request("GET", end_p + params)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response
                    response = connect.getresponse()

                    # -- Print the status line
                    print(f"Response from esembl received: {response.status} {response.reason}\n")

                    # -- Read the response:
                    body = response.read().decode("utf-8")

                    # -- We convert the body (str > dict):
                    all_s_dict = json.loads(body)

                    # -- We def. a list for the species in the dat. base species:
                    all_s_list = []

                    # -- We fix the display each specie name from the dictionary. Each name is a element of
                    # -- a list, representing the value of the key named species.

                    for k, v in all_s_dict.items():
                        if k == "species":
                            for element in v:
                                for k1, v1 in element.items():
                                    if k1 == "display_name":
                                        species = v1
                                        # -- We add every specie to all_s_list:
                                        all_s_list.append(species)

                    contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                    <title>List of species</title >
                                </head >
                                <body>
                                <p>Total number of species in the data base is: {len(all_s_list)}</p>
                                """

                    # -- We extract the order and the value from the input (limit):
                    lim_a = lim.split("=")[0]
                    lim_v = lim.split("=")[1]

                    if lim_a == "limit":

                        # -- Is a limit value is entered:
                        if lim_v != "":
                            contents += f"""<p>Number of species selected : {lim_v} </p>"""

                            # -- Invalid limit values:
                            if int(lim_v) > len(all_s_list) or int(lim_v) == 0 or int(
                                    lim_v) < 0:
                                contents = f"""<!DOCTYPE html>
                                                    <html lang = "en">
                                                    <head>
                                                        <meta charset = "utf-8" >
                                                        <title>ERROR</title >
                                                    </head>
                                                    <body>
                                                    <p>Limit out of range.
                                                    Introduce a valid limit </p>
                                                    </body></html>"""
                            else:
                                # -- We separate the first n species (n = lim ordered by the user)
                                limit_species_list = all_s_list[:(int(lim_v))]
                                contents += f"""<p>The species are: </p>"""

                                # -- Individual print of the species:
                                for species in limit_species_list:
                                    contents += f"""<p> > {species} </p>"""

                            contents += f"""<a href="/">Main page</a></body></html>"""

                        # -- If no limit input, all the species will be displayed:
                        else:
                            contents += f"""<p>No integer introduced. All species are going to be displayed. </p>
                                        <p>The species are: </p>"""

                            # The species are printed one by one:
                            for species in all_s_list:
                                contents += f"""<p> > {species} </p>"""
                            contents += f"""<a href="/">Main page</a></body></html>"""

                    else:
                        contents = Path('Error.html').read_text()

                except ValueError:
                    contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                 <meta charset = "utf-8" >
                                 <title>error</title >
                                </head>
                                <body>
                                <p>Error: You entered an invalid value. Introduce an integer value for limit</p>
                                <a href="/">Main page</a></body></html>"""

        except (KeyError, ValueError, IndexError, TypeError):
            contents = Path('error.html').read_text()
            contents += f"""<p><a href="/">Main page </a></body></html>"""

        # -- Gen. the resp. message
        self.send_response(status)  # -- Status line: OK!

        # -- Def. the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # -- The header is finished
        self.end_headers()

        # -- Send the response
        self.wfile.write(str.encode(contents))

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
        print("Stopped by the user")
        httpd.server_close()