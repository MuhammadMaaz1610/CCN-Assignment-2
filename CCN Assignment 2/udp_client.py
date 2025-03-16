#UDP client
import socket
import time

HOST = '127.0.0.2' 
PORT = 12346

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
total_time = 0
total_size = 0
lost_packets = 0

for i in range(100):    
    message = 'sent message '+ str(i)
    start_time=time.time()
    client.sendto(message.encode(),(HOST,PORT))
    client.settimeout(0.01)
    try:
        data ,addr = client.recvfrom(1024)
        print(data.decode())
        end_time=time.time()
        rtt=(end_time-start_time)*1000
        total_size = total_size + len(message) + len(data)
        total_time = total_time + rtt
    except socket.timeout:
        lost_packets = lost_packets +  1

print('Average time: ' + str(total_time/100)+'ms')
print('Thoughput: '+ str(total_size/(total_time))+' bits/ms')
print ('packet loss is: ' + str(lost_packets)+'%')
client.close()

