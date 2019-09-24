#!/usr/bin/python3

import sys
from time import sleep
from subprocess import getoutput

data=sys.argv[1:]
#sum=0
for i in data :
    print(getoutput("ping -c 3 "+i))
    #sleep(2)

#print(sum)

