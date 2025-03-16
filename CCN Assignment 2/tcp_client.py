#TCP CLIENT
import socket
import time

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST, PORT))
total_time = 0
total_size = 0

for i in range(100):
    message = 'sent message '+ str(i)
    start_time=time.time()
    client.send(message.encode())
    data=client.recv(1024).decode()
    print(data)
    end_time=time.time()
    rtt=(end_time-start_time)*1000
    total_size = total_size + len(message) + len(data)
    total_time = total_time + rtt

print('Average time: ' + str(total_time/100)+'ms')
print('Thoughput: '+ str(total_size/(total_time))+' bits/ms')
client.close()

