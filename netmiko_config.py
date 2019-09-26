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
print([ i for i in dir(device_connect) if 'send' in i])

# now sending config command

conf=['hostname pyrouter1','username hello privi 10 password cisco','router ospf 1']
output=device_connect.send_config_set(conf)
print(output)

# sending configuration from file

output1=device_connect.send_config_from_file('myR1.txt')
print(output1)

