from socket import *


def handle_request(connect_socket):
    data = connect_socket.recv(1024)

    file_read = open("index.html", "r")
    file_info = file_read.read()

    http_data = "HTTP/1.1 200 OK\r\n"
    http_data += "Content-Type:text/html\r\n"
    http_data +="\r\n"
    http_data += file_info

    connect_socket.send(http_data.encode())
    connect_socket.close()


def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(("127.0.0.1", 8000))
    tcp_socket.listen(5)

    while True:
        try:
            connect_socket, addr = tcp_socket.accept()
            print("Connect from ", addr)
            handle_request(connect_socket)
        except KeyboardInterrupt:
            break
    tcp_socket.close()


if __name__ == '__main__':
    main()
