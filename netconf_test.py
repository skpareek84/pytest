#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from ncclient import manager
import time
# Using connect function with manager to connect netconf enabled devices

device=manager.connect(host='172.16.43.153',username='root',password='cisco',port=22,allow_agent=False,look_for_keys=False,hostkey_verify=False)
print(device)
print('______________________')
print('______________________')
print(dir(device))
print('______________________')
time.sleep(1)
print(device.get_config('running'))

