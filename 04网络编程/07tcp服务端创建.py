from socket import socket

#1创建socket
so = socket(AF_INET,SOCK_STREAM)

#2绑定ip和端口
bindinfo = ("",7789)
so.bind(bindinfo)

#3调用listen转化为被动服务
so.listen(5)

#4.accept()生成客户端的socket和客户端ip端口信息

new_clent_socket,new_socket_ipprot = so.accept()

recvdata = new_clent_socket.recv(1024)
new_clent_socket.send("")
#5关闭客户端和服务端套接字
new_clent_socket.close()
so.close()