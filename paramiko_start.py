#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import paramiko
import time,sys
# using as ssh client

client=paramiko.SSHClient()

# auto adjust host key verification with yes or no

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# time for connecting to remote cisco ios
addr=input('enter your router ip : ')
u='root'
p='cisco'

# connecting with SSH session
client.connect(addr,username=u,password=p,allow_agent=False, look_for_keys=False)

# we have to ask for shell

device_access=client.invoke_shell()

# now sending command
device_access.send('show ip int brief \n')
time.sleep(2)
# assume command got executed and lets receive data

output=device_access.recv(65000)

# Decoding byte like string to string
print(output.decode('ascii'))


