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
        task = arguments[0]

        # -- Def. the contents and the status:
        contents = Path('Error.html').read_text()
        status = 200

        try:

            # -- Main page (index):
            if task == "/":
                contents = Path('index.html').read_text()

            # _______ Basic Lv. _______

            # -- List Species: List the names of all the species available in the database. Might be limited by the user
            # by entering a limit

            elif "/listSpecies" in task:

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

                    # -- We fix the display of each specie name from the dictionary. Each name is a element of
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

            # -- Return information about the karyotype of a specie: The name (usually a number) of all the chromosomes
            elif "/karyotype" in task:

                # -- We create a html 'template'
                contents = f"""
                    <!DOCTYPE html>
                    <html lang = "en">
                    <head>
                    <meta charset = "utf-8" >
                        <title>List of species</title >
                    </head >
                    <body>
                    """

                # -- We extract the specie selected:
                selection = arguments[1]

                # -- We separate the task and the name of this selection:
                sel_a = selection.split("=")[0]
                sel_n = selection.split("=")[1]

                # -- This endpoint lists:  -Current available assemblies
                # (w/ top level seq, chromosomes and cytogenetic bands).
                end_p = f"info/assembly/{sel_n}"

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

                    # -- We create a html 'template'
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

                    # -- We fix the karyotype from the dictionary. 'Karyotype is a key of the dict.
                    for k, v in all_s_dict.items():
                        if k == "karyotype":

                            # -- If the specie selected doesn't have a karyotype info in the data base:
                            if str(v) == "[]":
                                contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                    <title>Error</title >
                                </head >
                                <body>
                                <p> The resource req. is not available or doesn't exist</p>
                                """
                            else:
                                if sel_a == 'species':
                                    contents += f"""<p>The chromosomes requested are:</p>"""

                                    # -- 'v' is the list of values (karyotype). Individual print
                                    for i in v:
                                        contents += f"""<p> > {i} </p>"""
                                else:
                                    contents = Path("error.html").read_text()

                        # -- If the selected species doesn't exist or is not present in esembl:
                        elif f"{response.status} {response.reason}" == "400 Bad Request":
                            contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                                <title>Error</title >
                            </head >
                            <body>
                            <p> The resource req. is not available or doesn't exist</p>
                            """

                        # -- If no input is entered:
                        elif f"{response.status} {response.reason}" == "404 Not Found":
                            contents = Path("error.html").read_text()

                    contents += f"""<a href="/">Main page</a></body></html>"""

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

            # -- Return the Length of the chromosome named "chromo" of the given specie
            elif "/chromosomeLength" in task:

                # -- We extract the specie selected:
                selection = arguments[1]

                # -- 1) Obtained name of the species
                g_sel_species = selection.split("&")[0]
                sel_n = g_sel_species.split("=")[1]

                # -- 2) Chromosome:
                g_region_n = selection.split("&")[1]
                region_n = g_region_n.split("=")[1]

                # -- This endpoint lists:  -Info. from the specified top-level seq. of the selected species

                end_p = f"info/assembly/{sel_n}/{region_n}"

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

                    # -- We create a html 'template'
                    contents = f"""
                                                    <!DOCTYPE html>
                                                    <html lang = "en">
                                                    <head>
                                                    <meta charset = "utf-8" >
                                                        <title>List of species</title >
                                                    </head >
                                                    <body>
                                                    """

                    # -- We fix the karyotype from the dictionary. 'Karyotype is a key of the dict.
                    for k, v in all_s_dict.items():
                        if k == "length":
                            len_ch = str(v)
                            contents += f"""<p>The length of the selected chromosome is: {len_ch}</p>"""

                        # -- If the selected species doesn't exist or is not present in esembl:
                        elif f"{response.status} {response.reason}" == "400 Bad Request":
                            contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                                <title>Error</title >
                            </head >
                            <body>
                            <p> The resource req. is not available or doesn't exist</p>
                            """

                        # -- If no input is entered:
                        elif f"{response.status} {response.reason}" == "404 Not Found":
                            contents = Path("error.html").read_text()

                    contents += f"""<a href="/">Main page</a></body></html>"""

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
            # _______ Medium Lv. _______
            elif "/geneSeq" in task:

                # -- We extract the specie selected:
                selection = arguments[1]

                # --Obtain name of the species
                sel_n = selection.split("=")[1]

                # -- 1) This endpoint lists:  -Stable ID of the gene (human) + info
                end_p_1 = f"/xrefs/symbol/homo_sapiens/{sel_n}"

                try:

                    # Connect with the server
                    connect = http.client.HTTPConnection(server)

                    # -- Send the request message, using the GET method. The main page is requested
                    try:
                        connect.request("GET", end_p_1 + params)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response
                    response = connect.getresponse()

                    # -- Print the status line
                    print(f"Response from esembl received: {response.status} {response.reason}\n")

                    # -- Read the response:
                    body_1 = response.read().decode("utf-8")

                    # -- We convert the body (str > dict):
                    all_s_dict = json.loads(body_1)

                    # -- First element contains the stable ID:
                    dct_st = all_s_dict[0]

                    # -- Extraction of the stable ID:
                    st_id = dct_st["id"]

                    # -- 2) This endpoint lists:  -Complete seq of that gene (st_id)
                    end_p_2 = f"sequence/id/{st_id}"

                    # -- Send the request message, using the GET method. The main page is requested
                    try:
                        connect.request("GET", end_p_2 + params)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response
                    response_2 = connect.getresponse()

                    # -- Print the status line
                    print(f"Response from esembl received: {response_2.status} {response_2.reason}\n")

                    # -- Read the response:
                    body_2 = response_2.read().decode("utf-8")

                    # -- We convert the body (str > dict):
                    all_s_dict_2 = json.loads(body_2)

                    # -- Extraction of the seq.:
                    seq = all_s_dict_2["seq"]

                    # -- We create a html 'template'
                    contents = f"""
                                                    <!DOCTYPE html>
                                                    <html lang = "en">
                                                    <head>
                                                    <meta charset = "utf-8" >
                                                        <title>List of species</title >
                                                    </head >
                                                    <body>
                                                    """
                    # -- If the input is valid:
                    if f"{response.status} {response.reason}" == "200 OK" \
                            or f"{response_2.status} {response_2.reason}" == "200 OK":
                        contents += f"""<p>The seq. of {st_id} is: {seq}</p>"""

                    # -- If the selected species doesn't exist or is not present in esembl:
                    elif f"{response.status} {response.reason}" == "400 Bad Request":
                        contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                            <title>Error</title >
                        </head >
                        <body>
                        <p> The resource req. is not available or doesn't exist</p>
                        """

                    # -- If no input is entered:
                    elif f"{response.status} {response.reason}" == "404 Not Found":
                        contents = Path("error.html").read_text()

                    contents += f"""<a href="/">Main page</a></body></html>"""

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
            # -- Return information about a human gene: start, end, Length, id and Chromose
            elif "/geneInfo" in task:

                # -- We extract the specie selected:
                selection = arguments[1]

                # --Obtain name of the species
                sel_n = selection.split("=")[1]

                # -- 1) This endpoint lists:  -Stable ID of the gene (human) + info
                end_p_1 = f"/xrefs/symbol/homo_sapiens/{sel_n}"

                try:

                    # Connect with the server
                    connect = http.client.HTTPConnection(server)

                    # -- Send the request message, using the GET method. The main page is requested
                    try:
                        connect.request("GET", end_p_1 + params)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response
                    response = connect.getresponse()

                    # -- Print the status line
                    print(f"Response from esembl received: {response.status} {response.reason}\n")

                    # -- Read the response:
                    body_1 = response.read().decode("utf-8")

                    # -- We convert the body (str > dict):
                    all_s_dict = json.loads(body_1)

                    # -- First element contains the stable ID:
                    dct_st = all_s_dict[0]

                    # -- Extraction of the stable ID:
                    st_id = dct_st["id"]

                    # -- 2) This endpoint lists:  -Info of that gene/seq (st_id)
                    end_p_2 = f"lookup/id/{st_id}"

                    # -- Send the request message, using the GET method. The main page is requested
                    try:
                        connect.request("GET", end_p_2 + params)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response
                    response_2 = connect.getresponse()

                    # -- Print the status line
                    print(f"Response from esembl received: {response_2.status} {response_2.reason}\n")

                    # -- Read the response:
                    body_2 = response_2.read().decode("utf-8")

                    # -- We convert the body (str > dict):
                    all_s_dict_2 = json.loads(body_2)

                    # -- Extraction of the 'start' and 'end' values
                    start = all_s_dict_2["start"]
                    finish = all_s_dict_2["end"]
                    length = int(finish) - int(start)

                    id = all_s_dict_2["id"]
                    chromose = all_s_dict_2["seq_region_name"]

                    # -- We create a html 'template'
                    contents = f"""
                                                    <!DOCTYPE html>
                                                    <html lang = "en">
                                                    <head>
                                                    <meta charset = "utf-8" >
                                                        <title>List of species</title >
                                                    </head >
                                                    <body>
                                                    """
                    # -- If the input is valid:
                    if f"{response.status} {response.reason}" == "200 OK" \
                            or f"{response_2.status} {response_2.reason}" == "200 OK":
                        contents += f"""<h1>{sel_n}</h1>
                                    <p>Start Value: {start}</p>
                                    <p>End Value: {finish}</p>
                                    <p>Length Value: {length}</p>
                                    <p>Stable Id: {id}</p>
                                    <p>Chromose: {chromose}</p>"""

                    # -- If the selected species doesn't exist or is not present in esembl:
                    elif f"{response.status} {response.reason}" == "400 Bad Request":
                        contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                            <title>Error</title >
                        </head >
                        <body>
                        <p> The resource req. is not available or doesn't exist</p>
                        """

                    # -- If no input is entered:
                    elif f"{response.status} {response.reason}" == "404 Not Found":
                        contents = Path("error.html").read_text()

                    contents += f"""<a href="/">Main page</a></body></html>"""

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