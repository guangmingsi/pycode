from socket import *
client_list = []

def main():
	service_socket = socket(AF_INET,SOCK_STREAM)
	service_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	bind_info=("",7786)
	service_socket.bind(bind_info)
	service_socket.listen(1000)
	service_socket.setblocking(False)
	while True:
		try:
			new_socket,new_addr = service_socket.accetp()
		except:
			pass
		else:
			print("一个新的客户端到来%s:%s"%(str(new_addr),new_socket))
			new_socket.setblocking(False)
			client_list.appen((new_socket,new_addr))
		for client_socket,client_addr in client_list:
			try:
				recv_data = client_socket.recv(1024)
				if len(recv_data) > 0:
					print("%s:%s"%(str(client_addr),recv_data))
				else:
					print("客户端已经关闭")
					client_socket.close()
					client_list.remove((client_socket,client_addr))
			except:
				pass

if __name__ == '__main__':
	main()

