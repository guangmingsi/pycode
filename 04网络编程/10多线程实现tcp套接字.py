from threading import Thread 
from socket import *

def run(new_addr,new_socket):
	while True:
		recv_data = new_socket.recv(1024)
		if len(recv_data) >0:
			print("%s:%s"%(str(new_addr),recv_data))
		else:
			break
		new_socket.close()

def main():
	service_socket = socket(AF_INET,SOCK_STREAM)
	service_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	bindinfo=("",7799)
	service_socket.bind(bindinfo)
	service_socket.listen(5)
	try:
		while True:
			print("----主进程等待客户端-----")
			new_socket,new_addr = service_socket.accept()
			print("----多线程开始工作-------")
			clent_threading = Thread(target=run,args=(new_addr,new_socket))
			clent_threading.start()
	finally:
		service_socket.close()
if __name__ == '__main__':
	main()
