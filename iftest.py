#!/usr/bin/python3
from time import ctime,sleep
from subprocess import getoutput,getstatusoutput
from os import mkdir

options='''
Press 1 to  check current data and time :
Press 2 to run any command in current os :
Press 3 to create a dir :
Press 4 to ping any host :
'''

print(options)
choice = input()
print('you have chosen ', choice)
#int(choice)
if int(choice) == 1:
    print ('current date and time is', ctime())
elif choice == '2':
    cmd=input("please enter any command :")
    output=getoutput(cmd)
    print(output)
elif choice == '3' :
    cmd=input("Please give dir name :")
    mkdir(cmd)
    print(cmd," successfully created")
elif choice == '4' :
    host=input("enter host name to ping : ")
    print (getoutput("ping -c 5 "+host))
else :
    print ('please press correct option')

