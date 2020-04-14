import http.client
import json

serv = 'rest.ensembl.org'
end_p = '/info/ping'
prms = '?content-type=application/json'
url = serv + end_p + prms

print(f'Server: {serv}')
print(f'URL: {url}')

cnect = http.client.HTTPConnection(serv)

try:
    cnect.request('GET', end_p + prms)

except ConnectionRefusedError:
    print("Can't connect to the server")
    exit()

read = cnect.getresponse()

dat = read.read().decode()

resp = json.loads(dat)

ping = resp['ping']

if ping == 1:
    print(f'Ping Ok! The dat.base is running')
