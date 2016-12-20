import socket
client_socket = socket.socket()
print("Please enter your name")
name = input()
client_socket.connect(('127.0.0.1',2222))
client_socket.send(bytes(name,'utf-8'))
data = client_socket.recv(1000)
data = data.decode('utf-8')
print(data.decode('utf-8'))
