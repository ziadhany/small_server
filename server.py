#!/usr/bin/python3           # This is server.py file
import socket                                         
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 9999                                           
serversocket.bind((host, port))                                  
serversocket.listen(5)                                           
clientsocket,addr = serversocket.accept()     
print("Got a connection from %s" % str(addr)) 
while True:
    msg = input("server:-->")
    clientsocket.send(msg.encode('ascii'))
    result =  clientsocket.recv(1024)
    print(result.decode('ascii'))
    if msg == "exit":
        break
clientsocket.close()