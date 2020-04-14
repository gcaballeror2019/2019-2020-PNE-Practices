import http.client
import json
import termcolor
from Seq1 import Seq
GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

bases = ['A', 'T', 'C', 'G']
gene_n = input('Enter the name of a gene:')
server = 'rest.ensembl.org'
end_p = '/sequence/id/'
params = '?content-type=application/json'
REQ = end_p + GENES[gene_n] + params
URL = server + REQ

print()
print(f'Server: {server}')
print(f'URL: {URL}')

# Connect with the server
cnect = http.client.HTTPConnection(server)

try:
    cnect.request('GET', REQ)

except ConnectionRefusedError:
    print('ERROR! Cannot connect to the Server')
    exit()

# -- Read the response message from the server
rd = cnect.getresponse()

# -- Print the status line
print(f'Response received!: {rd.status} {rd.reason}\n')

# -- Read the response's body
dat = rd.read().decode()

# -- Create a variable with the data,
# -- form the JSON received
resp = json.loads(dat)

termcolor.cprint('Gene', 'green', end='')
print(f': {gene_n}')
termcolor.cprint('Description', 'green', end='')
print(f": {resp['desc']}")

g_str = resp['seq']

s = Seq(g_str)

str_len = s.len()

Num = s.count_base()
Per_A = '{:.1f}'.format(100 * int(Num[0]) / str_len)
Per_C = '{:.1f}'.format(100 * int(Num[1]) / str_len)
Per_T = '{:.1f}'.format(100 * int(Num[2]) / str_len)
Per_G = '{:.1f}'.format(100 * int(Num[3]) / str_len)

termcolor.cprint('Total Length', 'green', end='')
print(f": {str_len}")

termcolor.cprint('A', 'blue', end='')
print(f': {Num[0]} ({Per_A}%)')

termcolor.cprint('C', 'blue', end='')
print(f": {Num[1]} ({Per_C}%)")

termcolor.cprint('G', 'blue', end='')
print(f": {Num[2]} ({Per_G}%)")

termcolor.cprint('T', 'blue', end='')
print(f': {Num[3]} ({Per_T}%)')

m = max(Num)

termcolor.cprint('Most frequent', 'green', end='')
print(f': {m}')