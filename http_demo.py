from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(("127.0.0.1", 8000))
tcp_socket.listen(5)

connect_socket, addr = tcp_socket.accept()
print("Connect from ", addr)

data = connect_socket.recv(1024)
print(data.decode())

file_read = open("index.html", "rb")

http_data = """HTTP/1.1 200 OK
Content-Type:text/html

%s
""" % (file_read.read().decode())

connect_socket.send(http_data.encode())
connect_socket.close()
tcp_socket.close()
