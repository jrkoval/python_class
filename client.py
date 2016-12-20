import socket
from myparser import Handler

client_socket = socket.socket()

client_socket.connect(('127.0.0.1', 5556))

client_socket.send(bytes('land', 'utf-8'))

data = client_socket.recv(1000)
xml.sax.parseString(data,Handler())

#print(data.decode('utf-8'))

