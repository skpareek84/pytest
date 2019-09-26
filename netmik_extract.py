#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from netmiko import ConnectHandler

cisco_csr = {
	'device_type' : 'cisco_ios',
	'host' : '172.16.43.153',
	'username' : 'root',
	'password' : 'cisco'
}

# By checking couple of things connecthandler will allow you to connect
'''
	. device_type
'''

device_connect= ConnectHandler(**cisco_csr)

#print(dir(device_connect))
#print([ i for i in dir(device_connect) if 'send' in i])

# now sending command
#cmd=['show ip int brief', 'show ippp']

output=device_connect.send_command('show int gi1',use_textfsm=True)
print(output)
