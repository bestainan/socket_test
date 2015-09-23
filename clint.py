#-*- coding : UTF-8 -*-

import socket

HOST = '192.168.1.106' 
PORT = 9999            

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

num = input('input a number: ')
s.send(num.encode())
data = s.recv(1024)
     
print('Received', data.decode()) #返回的是字节型  所以要用encode()编码  decode() 解码

s.close()