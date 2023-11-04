import socket

#create socket object 
s = socket.socket()
print("Socket successfully created")
port=12345
s.bind('',port)
print("socket binded to %s" %(port))

#put the socket into listening mode 
s.listen(5)
print("socket is listening ")

#forever loop 
while True:

#Establish connection with client 
    c,addr = s.accept()
    print('got connection from',addr)
    c.send(b'Thank you for connecting')

    c.close()