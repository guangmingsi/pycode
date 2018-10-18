import sys
from socket import *

def = ("<broadcast>",7788)

#创建套接字

s = socket(AF_INET,SOCK_DGRAM)

#创建广播

s = setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.sendto("hi",dest)

