import socket
import threading

class Mythread(threading.Thread):
    def __init__(self,client):
        threading.Thread.__init_(self)
        self.client = client
    def run(self):
        data = self.client.recv(100)
        data = data.decode('utf-8')
        data = "Hello " +data
        self.client.send(bytes(data, 'utf-8'))

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 5556))
server_socket.listen(3)

while True:
    client, addr = server_socket.accept()
    t1 = Mythread(client)
    t1.start()
    
