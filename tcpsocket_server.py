#!/usr/bin/env python
# coding=utf-8
import time
from socket import *
import threading

def tcplink(sock,addr):
    print 'accept new connection from %s:%s...' % addr
    sock.send('Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('hello,%s!'% data)
    sock.close()
    print 'connection from %s:%s closed' % addr
    

s = socket(AF_INET,SOCK_STREAM)
HOST = ''
PORT = 12306
ADDR = (HOST,PORT)
s.bind(ADDR)
s.listen(5)
print 'waiting for connection...'
#通过一个永久循环来接受来自客户端的连接
while True:
    sock,addr = s.accept()
    #创建新线程来处理TCP的连接
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

