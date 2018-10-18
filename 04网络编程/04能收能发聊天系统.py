#倒入模块，多线程，socket
from threading import Thread 
from socket import *

#创建发送消息函数
def sendmsg():
	while True:
		send_content = input()
		udp_socket.sendto(send_content.encode("utf-8"),send_addr)
		if send_content == "再见":
			udp_socket.close()
			break

def recvmsg():
	while True:
		recv_data = udp_socket1.recvfrom(1024)
		print("[%s]\r%s "%(str(recv_data[1]),recv_data[0].decode("utf-8")))
		if recv_data[0] == "再见":
			udp_socket1.close()
			break


#创建收消息函数
udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket1 = socket(AF_INET,SOCK_DGRAM)
send_addr = ("192.168.50.131",3331)
self_info = ("",3330)
udp_socket1.bind(self_info)
#创建多线程去执行发消息，和收
thread1 = Thread(target=sendmsg)
thread1.start()
thread2 = Thread(target=recvmsg)
thread2.start() 
#创建udpsocket

