#! /usr/bin/python3.4
#-*- coding : UTF-8 -*-
import socketserver

class myTCPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(4096)
        print self.data
        
        self.request..sendall(self.data.upper())
        
if __name__ == '__main__':
    h,p = '',9999
    server = socketserver.TCPServer((h,p), myTCPHandler)
    server.serve_forever()
