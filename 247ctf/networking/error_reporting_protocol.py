from scapy.all import *
pcap = rdpcap('error_reporting.pcap')
# create the jpg file to write data to
file = open('winner.jpg','wb')
# writing the payloads of the ICMP packets to the file
for i in range(1,1712):
	file.write(pcap[ICMP][i].load)
