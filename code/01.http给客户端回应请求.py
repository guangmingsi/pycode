import socket

from multiprocessing import Process

def handle_client(cli_socket):
	"""处理客户端请求"""
	# 接收客户端请求数据
	recvdata = cli_socket.recv(1024)
	print("收到数据%s"%recvdata)

	# 构造相应数据
	response_startline = "HTTP/1.1 200 ok\r\n"
	response_headers = "Server: My server\r\n"
	response_body = "触控要完"
	response = response_startline + response_headers + "\r\n" + response_body
	print("response data:",response)

	# 返回给客户端请求
	cli_socket.send(bytes(response, "gb2312"))
	cli_socket.close()


def main():
	HTML_ROOT_DIR = ""
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind(("", 1522))
	server_socket.listen(100)
	try:
		while True:
			cli_socket , cli_addr = server_socket.accept()
			p = Process(target=handle_client,args=(cli_socket,))
			p.start()
			cli_socket.close()
	except:
		pass
	finally:
		server_socket.close()
if __name__ == '__main__':
	main()
