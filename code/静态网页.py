import re
import socket
import os
from multiprocessing import Process

HTML_ROOT_DIR ="./"

def fun(cli_socket):
    recvdata = cli_socket.recv(1024)
    # 获取请求内容
    print(recvdata)
    print(type(recvdata))
    recvdata_line = recvdata.splitlines()
    for i in recvdata_line:
        print(i)


    # "GET / HTTP 1.0"
    require_start_line = recvdata_line[0]
    file_name =re.match(r"\w+ +(/[^ ]*)",require_start_line.decode("utf-8")).group(1)
    print("---1----" ,file_name)
    if "/" == file_name:
        file_name = "index.html"
        print("******",file_name)
    try:
        f = open(HTML_ROOT_DIR+file_name, "rb")
        print("----2-----",HTML_ROOT_DIR+file_name)
    except IOError:
        response_start_line = "HTTP /1.1 404 Not Found\r\n"
        response_sever = "Server: My server\r\n"
        response_body = "The file is not found"
    else:
        read_file1 = f.read()
        print("--------",read_file1)
        response_body = read_file1.decode("utf-8")
        f.close()
    finally:
    # 构造响应体
        response_start_line = "HTTP /1.1 200 OK\r\n"
        response_sever = "Sever: My server\r\n"
        send_response = response_start_line + response_sever + "\r\n"+ response_body
        cli_socket.send(bytes(send_response,"utf-8"))

    # 关闭套接字
        cli_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("",7719))
    server_socket.listen(128)
    while True:
       cli_socket, cli_addr = server_socket.accept()
       t = Process(target=fun, args=(cli_socket,))
       t.start()
       cli_socket.close()

if __name__ == "__main__":
    main()