#导入模块
from socket import *
#创建tcp套接字
tcp_clent = socket(AF_INET,SOCK_STREAM)
#调用connect方法
tcp_clent.connect(("192.168.1.10",2227))
#发送数据send
tcp_clent.send("sfasdf")
#接收数据recv
tcp_clent.recv(1024)
#关闭
tcp_clent.close()	