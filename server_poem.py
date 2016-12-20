import socket
import re
import poem
import xml.dom.minidom

#if __name__ == "__main__":
    
   

doc = xml.dom.minidom.Document()
cities = doc.createElement('cities')
cities.setAttribute("total","1")
city = doc.createElement('city')    
text = doc.createTextNode('London')
city.appendChild(text)
cities.appendChild(city)
doc.appendChild(cities)
print(doc.toprettyxml())
#We are creating an object of class socket defined in the module called socket

server_socket = socket.socket()

#sockets as interface between applications running on two diferent systems
# ip adress and port number respond to this ip address and respond to resquests that
# only come on port 5555
server_socket.bind(('127.0.0.1',5556))
# only 3 clients can connect to this server
server_socket.listen(3)
# accepts the tuple from above
# client is a socket
client,addr = server_socket.accept()

#server will ask client to send some data
# return bytes that are converted to strings by decode

data = client.recv(1000)
data = data.decode('utf-8')

#init function of the poem module will be invoked
#it reads the file 'poem.txt' and loads into a list
p1 = poem.Poem()
#p1.removePunctuation()
result= p1.getLines(data)
'''
# ['land',(4,'This is my own land'] not bytes or strings
# need to convert to string; put in quotes
# and convert to bytest but the parsing at client is difficult
# and only python can understand this data structure
# if server is written in python, client has to run in python
# should have this restriction, should be able to be able to
# implement client in any language, ruby, php, etc.
# should send in program independent format json or xml
# 1. There is a document
#2. There will be a root element and there need to be only ONE root element
#3. There could be multiple elements
#Document
#   Root Element
#     Element1
#     Element2
#<cities total 2>
#   <city>
#      London

    </city>
    <city>
       Mysore
    </city>
</cities>
'''
#data = "Hello " +data
data = doc.toxml()
client.send(bytes(data, 'utf-8'))


#generate thois xml
# send it to the client
'''
<lines total="1" words="land">
    <line linenumber="4">
        This is my land
    </line>
</lines>
'''
