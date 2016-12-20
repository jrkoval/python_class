import socket

#We are creating an object of class socket defined in the module called socket

server_socket = socket.socket()

#sockets as interface between applications running on two diferent systems
# ip adress and port number respond to this ip address and respond to resquests that
# only come on port 5555
server_socket.bind(('127.0.0.1',5555))
# only 3 clients can connect to this server
server_socket.listen(3)
# accepts the tuple from above
# client is a socket
client,addr = server_socket.accept()

#server will ask client to send some data
# return bytes that are converted to strings by decode

data = client.recv(100)
data = data.decode('utf-8')

data = "Hello " +data
client.send(bytes(data, 'utf-8'))
