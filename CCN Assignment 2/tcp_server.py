#TCP SERVER
import socket
import time

HOST = '127.0.0.1' 
PORT = 12345

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST, PORT))
print('Server is listening... ')
server.listen(100)

while True:
    client, addr = server.accept()
    
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        print(data)
        client.send(('Recieved: '+ data).encode())
    
    client.close()

