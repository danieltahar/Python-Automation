import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9090))
s.send('hello world')

data = s.recv(1024)
s.close()