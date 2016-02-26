# -*- coding: UTF-8 -*-

from socket import *

HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcp_client_fd = socket(AF_INET, SOCK_STREAM)
tcp_client_fd.connect(ADDR)

try:
    while True:
            data = raw_input('type close to exit >')
            if data == 'close':
                break
            if not data:
                continue
            tcp_client_fd.send(data)
            data = tcp_client_fd.recv(BUFSIZE)
            print data
except:
    tcp_client_fd.close()
