from scapy.all import send, IP, TCP, ICMP, UDP
send(IP(dst='localhost')/TCP(dport=53, flags='S'))
