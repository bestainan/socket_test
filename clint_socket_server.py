# -*- coding: UTF-8 -*-
import socket
import sys

HOST, PORT = "192.168.1.106", 8888
data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    sock.connect((HOST, PORT))
    sock.sendall(b'HI')
    received = sock.recv(1024)

    sock.close()
    print(received)

