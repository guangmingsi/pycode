from socket import *

#创建一个udp
so = socket(AF_INET,SOCK_DGRAM)
port_info = ("",8989)
so.bind(port_info)
while True:
	recvdata = so.recvfrom(1024)
	recv_content = recvdata[0]
	print(recv_content.decode("utf-8"))
	if recv_content.decode("utf-8") =="再见":
		break
print("程序关闭")