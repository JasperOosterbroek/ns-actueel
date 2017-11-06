import requests
print (dir(requests))

r = requests.get('http://webservices.ns.nl/ns-api-avt?station=ut', auth=('jasper.oosterbroek@student.hu.nl', 'JXwCrdq5iel_il2lLgaWhq-3AtpqZ-2r1s_UC0CLIc72XN9G7aM5vg'))
if r.status_code == '200':
    # good response
    print(r.text)