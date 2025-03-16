#UDP SERVER
import socket
import random

HOST = '127.0.0.2' 
PORT = 12346

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print('Server is listening... ')

while True:
    data, addr = server.recvfrom(1024)
    data_2=data.decode()
    print(data_2)
    message = 'Recieved: ' + data_2
    if random.random()>0.2:
        server.sendto(message.encode(),addr)
    else:
        print('Dropped packet')


