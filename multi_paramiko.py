#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import paramiko
import time,sys
# using as ssh client

client=paramiko.SSHClient()

# auto adjust host key verification with yes or no

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# time for connecting to remote cisco ios
#addr=sys.argv[1] # first argument for IP
#u=sys.argv[2]
#p=sys.argv[3]
device_ip=['172.16.43.153','172.16.43.153','172.16.43.153']
u='root'
p='cisco'

for i in device_ip :
	# connecting with SSH session
	client.connect(i,username=u,password=p,allow_agent=False, look_for_keys=False)
	# we have to ask for shell
	device_access=client.invoke_shell()
	# now sending command
	device_access.send('terminal len 0 \n')
	device_access.send('show run \n')
	time.sleep(1)
	# assume command got executed and lets receive data
	output=device_access.recv(65000)
	# Decoding byte like string to string
	print(output.decode('ascii'))
	print('__________________________')
	print('__________________________')
	with open(i+time.ctime(),'w') as f:
		f.write(output.decode('ascii'))
		time.sleep(1)

# now want to save this output in a file


