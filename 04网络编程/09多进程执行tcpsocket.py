from multiprocessing import Process
from socket import *

def run(new_socket,new_addr):
	while True:
		recvdata = new_socket.recv(1024)
		if len(recvdata) >0:
			print("%s:%s"%(str(new_addr),recvdata.decode("utf-8")))
		else:
			break
	new_socket.close()

def main():
	#创建tcp套接字
	service_socket = socket(AF_INET,SOCK_STREAM)
	#套接字重复使用地址
	service_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	bind_info=("",7788)
	service_socket.bind(bind_info)
	service_socket.listen(5)
	try:
		while True:
			print("---主进程，等待客户端连接---")
			new_socket,new_addr = service_socket.accept()
			client_process = Process(target=run,args=(new_socket,new_addr))
			client_process.start()
			#子进程已经复制，可以关闭进程
			new_addr.close()
	finally:
		service_socket.close()

if __name__ == '__main__':
	main()
