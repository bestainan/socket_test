import socket

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))#绑定
s.listen(1) #监听数量
conn, addr = s.accept()  #监听 接收 外部连接


print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
