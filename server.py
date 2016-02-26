# -*- coding: UTF-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcp_server_fd = socket(AF_INET, SOCK_STREAM)
tcp_server_fd.bind(ADDR)
tcp_server_fd.listen(5)

while True:
    print 'Waiting for connection ...'
    tcp_client_fd, addr = tcp_server_fd.accept()
    print '>Connected from:', addr
    
    while True:
        try:
            data = tcp_client_fd.recv(BUFSIZE)
            print '<',data
            tcp_client_fd.send('[%s] %s'% (ctime(),data))
        except:
            print '#Disconnect from:',addr
            tcp_client_fd.close()
            break
tcp_server_fd.close()

            
