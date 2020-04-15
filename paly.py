"""
web server

提供一个服务端使用类,通过这个类可以快速的搭建一个web server服务,用以展示自己的简单网页
"""

from socket import *
from select import select

#　主体功能　
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=80,html=None):
        self.host = host
        self.port = port
        self.html = html
        # 多路服用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 创建套接字和地址绑定工作
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setblocking(False)

    def bind(self):
        self.address = (self.host,self.port)
        self.sockfd.bind(self.address)

    # 启动服务 准备接受链接的过程
    def start(self):
        self.sockfd.listen(3)
        print("Listen the port %s"%self.port)
        # select TCP并发服务
        self.rlist.append(self.sockfd)
        while True:
            # 对IO进行监控
            rs,ws,xs = select(self.rlist, self.wlist, self.xlist)
            # 遍历列表分情况讨论
            for r in rs:
                if r is self.sockfd:
                    # 监听套接字就绪
                    c, addr = r.accept()
                    print("Connect from", addr)
                    # 添加客户端链接套接字作为监控对象
                    c.setblocking(False)
                    self.rlist.append(c)
                else:
                    # 客户端链接套接字就绪
                    self.handle(r)

    # 对每一个客户端请求的具体处理
    def handle(self,connfd):
        # 接受客户端请求
        request = connfd.recv(1024)
        print(request)


if __name__ == '__main__':
    """
    通过HTTPServer类快速搭建服务
    static中有一组网页,我为了展示我的这组网页
    """

    # 需要使用者提供 : 网络地址   网页位置
    host = "0.0.0.0"
    port = 8000
    dir = "./static"

    # 实例化对象
    httpd = HTTPServer(host=host,port=port,html=dir)

    # 调用方法启动服务
    httpd.start()
