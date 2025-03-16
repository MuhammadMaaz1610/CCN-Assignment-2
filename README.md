# CCN-Assignment-2
TCP
    RUNNING:
        Go to Terminal and run tcp_server.py by writing python tcp_server.py
        Go to Terminal and run tcp_client.py by writing python tcp_client.py
        record outputs
    EXPECTED OUTPUTS:
        should output "Recieved: send message n" where n in increacing from 0 to 99
        then output is average time which should range around 0.6ms
        then output will be throughput which will range around 60 to 75 bits per ms

UDP
    RUNNING:
        Go to Terminal and run udp_server.py by writing python udp_server.py
        Go to Terminal and run udp_client.py by writing python udp_client.py
        record outputs
    EXPECTED OUTPUTS:
        should output "Recieved: send message n" where n in incracing from 0 to 99 with some numbers missing symbolisiing packets lost
        then output is average time which should range around 0.45ms
        then output will be throughput which will range around 60 bits per ms
        packet loss is around 20%

RESOURCES:
    I watched a youtube video https://www.youtube.com/watch?v=fWjsdhR3z3c for python basics and a youtube video https://www.youtube.com/watch?v=bwTAVGg_kVs to understand basics of udp and tcp and geeksforgeeks.org for socket and for syntax for other parts such as random and time 

COMPARASION AND ANAYSIS:
    1.Average rtt for tcp is around 0.6ms and 0.45ms for udp. udp is quicker as is has less as it doesnt have as high of overhead 
    2.packet is not reached as udp doesnt account for errors resulting in retransmission, tcp ensure all packets arrive correctly for tasks that requre all data without loss
    3.tcp is better for bulk transfer as it has greater throughput. it introduced overhead to ensure data is received
    4.when data integrity does not matter use udp as it is faster such as real time video and audio but in cases where data integrity matters use tcp such as emails
