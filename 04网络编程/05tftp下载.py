import struct
from socket import *
import sys
#创建一个文件存储下载的内容
file_name = input("要下载的文件名：---")
#创建socket
udp_socket = socket(AF_INET,SOCK_DGRAM)
ip_addr = input("输入ip地址")
port_num = int(input("输入端口号"))
send_server_addr = (ip_addr,port_num)

#发送请求，要转换成大端
sendrequest = struct.pack("!H%dsb5sb"%len(file_name),1,file_name,0,"octet",0)
udp_socket.sendto(sendrequest,send_server_addr)
#服务器给我返回了一个数据包，我要解析，写入本地文件
p_num = 0
while True:
	recvData,recvAddr = udp_socket.recvfrom(1024)
	recvDatalen = len(recvData)
	#解析数据包
	recvData_tuple = struct.unpack("!HH",recvData[:4])
	cmd = recvData_tuple[0]
	recvData_num = recvData_tuple[1]
#给服务器发送确认请求ack，不是错误的就发送确认，错误的发送错误
	if cmd == 3:
		if recvData_num ==1:
			f = open(file_name,"a")
		#判断是否是下一个包
		if p_num+1 ==recvData_num:
			f.write(recvData[4:])
			p_num +=1
			ACK = struct.pack("!HH",4,recvData_num)
			udp_socket.sendto(ACK,recvAddr)
		if recvDatalen <516:
			recvFile.close()
			print("下载完成")
			break
	elif cmd == 5:
		print("error")
		break
	udp_socket.close()





