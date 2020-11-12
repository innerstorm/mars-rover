import socket
import sys
import time

x = socket.socket()
host_name = input(str('Server hostname:'))
#host_name = socket.gethostname()
port = 8080

x.connect((host_name, port))
print('Connected to server')

while True: 
    incoming_message = x.recv(1024)
    incoming_messagge = incoming_message.decode()
    
    print("Server incoming message: ", incoming_message)
    
    message = input(" >> ")
    message = message.encode()
    
    x.send(message)
    print("message has been sent...")