import socket
import sys 
import time

x = socket.socket()
host_name = socket.gethostname()
print('server will start on host: ', host_name)
port = 8080

x.bind((host_name, port))

print("server done binding to host and port successfully")
print("server is waiting for incoming connections...")

x.listen(1)

connection, address = x.accept()

print(address, " has connected to the server and is now online...")

while True:
    display_mess= input(str(" >> "))
    display_mess=display_mess.encode()
    connection.send(display_mess)
    print("message has been sent...")
    in_message=connection.recv(1024)
    in_messagge=in_message.decode()
    print("Client says: ", in_message)