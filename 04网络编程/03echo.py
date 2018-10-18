from socket import *

#创建一个udp
so = socket(AF_INET,SOCK_DGRAM)
port_info = ("",8989)
so.bind(port_info)
n=0
while True:
	recvdata = so.recvfrom(1024)
	recv_content = recvdata[0]
	so.sendto(recv_content,recvdata[1])
	n+=1
	print(recv_content.decode("utf-8")+"已返回数据%d"%n)
	if recv_content.decode("utf-8") =="再见":
		so.close()
		break
print("程序关闭")