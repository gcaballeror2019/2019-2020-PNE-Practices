from pathlib import Path
import http.server
import termcolor
import socketserver
from Seq1 import Seq

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

seq_num = [
    'ACTAAACTGATCGATGCTAGCTAGTCGATGCTAG',
    'TCTTGCGTAGCTGTGATGCTTTTGGACGTGTAGC',
    'ATCGACTCGATTTAAAACTGATCGATCGATCGAT',
    'ACTGGATCTTACCCATCGTAGCTAGTGCTAGCTG',
    'AAAAAGCTTTACTGTACGTAGCATGGCTGTCAGC'
]
folder = r'C:\\Users\\Usuario\\PycharmProjects\\2019-2020-PNE-Practices2\\Session04\\'
ext = '.txt'


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

        # -- Gives a response depending of the existence of de
        if verb == '/':
            # OPen form-1 file (HTML)
            contents = Path('form-4.html').read_text()
            # Status code
            status = 200
        elif verb == '/ping':
            # Verification page to show that the server is on-line
            contents = '''
                        <!DOCTYPE html>
                        <html lang='en'>
                        <head>
                            <meta charset='utf-8'>
                            <title>PING</title>
                        </head>
                        <body>
                        <h2> Ping Ok! </h2>
                        <p> The Seq2 server is running correctly... </p>
                        <h2>Received message:</h2>
                        <a href='/'>Main page</a>
                        </body>
                        </html>
                        '''
            status = 200
        elif verb == '/get':
            pair = arguments[1]
            tpe = pair.split('?')
            ind, value = tpe[0].split('=')
            n = int(value)
            # -- Get sequence
            seq = seq_num[n]

            # -- HTML
            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> GET </title >
                        </head >
                        <body>
                        <h2> Sequence number {n}</h2>
                        <p> {seq} </p>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            status = 200

        elif verb == '/gene':
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, gene = pairs[0].split('=')

            s = Seq()
            s = s.read_fasta(folder + gene)
            gene_str = str(s)
            # -- Generate the html code
            contents = f"""
                                   <!DOCTYPE html>
                                   <html lang = "en">
                                   <head>
                                   <meta charset = "utf-8" >
                                     <title> GENE </title >
                                   </head >
                                   <body>
                                   <h2> Gene: {gene}</h2>
                                   <textarea readonly rows="20" cols="80"> {gene_str} </textarea>
                                   <br>
                                   <br>
                                   <a href="/">Main page</a>
                                   </body>
                                   </html>
                                   """
            status = 200
        elif verb == '/operation':
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value, and the operation name w/ the chosen operation
            name, seq = pairs[0].split('=')
            o_name, operation = pairs[1].split('=')
            seq = Seq(seq)
            if operation == 'Rev':
                result = seq.reverse()
            elif operation == 'Comp':
                result = seq.complement()
            else:
                # We calculate the length, amount of bases and the percentage they occupy in the sequence
                g_len = seq.len()
                counter = seq.count()
                per_a = 100 * int(counter['A']) / g_len
                per_c = 100 * int(counter['C']) / g_len
                per_t = 100 * int(counter['T']) / g_len
                per_g = 100 * int(counter['G']) / g_len
                result = f"""
                    <p>Total length: {g_len}</p>
                    <p>A: {counter['A']} ({per_a}%)</p>
                    <p>C: {counter['C']} ({per_c}%)</p>
                    <p>G: {counter['T']} ({per_t}%)</p>
                    <p>T: {counter['G']} ({per_g}%)</p>"""
            contents = f"""
                <!DOCTYPE html>
                <html lang = "en">
                <head>
                <meta charset = "utf-8" >
                    <title> Operations </title >
                </head >
                <body>
                <h2> Seq:</h2>
                <p>{seq}</p>
                <h2> Operation: </h2>
                <p>{operation}</p>
                <h2> Result: </h2>
                <p>{result}</p>
                <br>
                <br>
                <a href="/">Main page</a>
                </body>
                </html>
                """
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

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('')
        print('Stopped by the user')
        httpd.server_close()
