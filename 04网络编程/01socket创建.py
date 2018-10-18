# -*- coding: utf-8 -*-
from socket import *

#创建一个socket对象
s = socket(AF_INET,SOCK_DGRAM)#创建一个udpsocket对象
#创建一个tcp套接字
#s= socket(AF_INET,SOCK_STREAM)
bindAddr = ("",7788)
s.bind(bindAddr)#绑定端口，才能接收
#ipaddr = ("192.168.50.131",8080)
sendcontent=("hahaha")
s.sendto(sendcontent.encode("utf-8"),ipaddr)#python3中字符串前面要加b
recevdate=s.recvfrom(1024) #接受数据代码
print(recevdate)#打印接受数据

s.close()