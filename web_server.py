from socket import *
from select import *


class HttpServer:
    def __init__(self, host="0.0.0.0", port=8000, path="./"):
        self.__HOST = host
        self.__PORT = port
        self.__path = path
        # 创建套接字和地址绑定工作
        self.__create_socket()
        self.__bind_socket()
        self.__ep = epoll()
        self.__ep.register(self.__tcp_socket, EPOLLIN | EPOLLET)
        self.__dict_fn = {self.__tcp_socket.fileno(): self.__tcp_socket}

    @property
    def ADDR(self):
        return self.__ADDR

    def __create_socket(self):
        self.__tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.__tcp_socket.setblocking(False)

    def __bind_socket(self):
        self.__ADDR = (self.__HOST, self.__PORT)
        self.__tcp_socket.bind(self.__ADDR)

    def __send_html(self):
        pass

    def __socket_connect(self):
        connect_socket, addr = self.__tcp_socket.accept()
        print("Connect from ", addr)
        self.__ep.register(connect_socket, EPOLLIN | EPOLLET)
        self.__dict_fn[connect_socket.fileno()] = connect_socket

    def __server_handler(self, connect_socket):
        data = connect_socket.recv(1024)

    def start(self):
        self.__tcp_socket.listen(5)
        print("Listen the port %s" % self.__PORT)
        while True:
            try:
                events = self.__ep.poll()
                for item in events:
                    project = self.__dict_fn[item[0]]
                    if project is self.__tcp_socket:
                        self.__socket_connect()
                    else:
                        self.__server_handler(project)
            except KeyboardInterrupt:
                break
        self.__tcp_socket.close()


if __name__ == '__main__':
    host = "0.0.0.0"
    port = 8000
    path = "./static/"
    http_server = HttpServer(host=host, port=port, path=path)
    http_server.start()
