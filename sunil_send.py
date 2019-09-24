#!usr/bin/python3

import socket,time

#checking for socket function

print([i for i in dir(socket) if 'socket' in i])

# Now creating UDP socket
# ipv4 socket -- ipv4 add + 2 byte port
# ipv6 socket -- ipv6 add + 2 byte port

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# enter message
while True :
    msg=input('enter data to send : ')
    # lets send data to target
    #convert message to byte like stream
    newmsg=msg.encode('ascii')
    s.sendto(newmsg,('127.0.0.1',8899))
    data=s.recvfrom(10000)
    print(data)

s.close()
