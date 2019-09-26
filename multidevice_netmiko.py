#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from netmiko import ConnectHandler
from getpass import getpass
import netmiko
sec=getpass('Plz enter your password : ')
cisco_csr1 = {
	'device_type' : 'cisco_ios',
	'host' : '172.16.43.153',
	'username' : 'root',
	'password' : sec
}

cisco_csr2 = {
	'device_type' : 'cisco_ios',
	'host' : '172.16.43.154',
	'username' : 'cisco',
	'password' : sec
}

cisco_csr3 = {
	'device_type' : 'cisco_ios',
	'host' : '172.16.43.153',
	'username' : 'root',
	'password' : sec
}
# By checking couple of things connecthandler will allow you to connect
'''
	. device_type
'''




for i in [cisco_csr1,cisco_csr2,cisco_csr3]:
	try :
		#print ('sending command ', i)
		#print ('-------------------')
		print('Connecting with Router :---> ',i['host'])
		device_connect=ConnectHandler(**i)
		output=device_connect.send_command('show ip int brief')
		print(output)

	except netmiko.ssh_exception.NetMikoAuthenticationException :
		print(' Please check your ip or password ',i['host'])


