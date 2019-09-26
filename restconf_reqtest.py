#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import requests

from requests.auth import HTTPBasicAuth

# this is for supplying http basic auth

cred=HTTPBasicAuth('root','cisco')

h={'Accept':'application/json'}

#headers={'Accept':'text/html'}

# defining data from that API in JSON

url="http://172.16.43.153/level/15/exec/-/sh/ip/int/brief"

# Now connection to restconf or http protocol

output=requests.get(url,headers=h,auth=cred)

print(output)

# Print HTML based response

print(output.text)
