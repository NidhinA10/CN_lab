import socket
import struct

# Create raw socket
sock = socket.socket(
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.ntohs(3)
)

print("RAW SOCKET PACKET CAPTURE STARTED...\n")

try:
    while True:
        packet, addr = sock.recvfrom(65535)

        # IP header starts after 14-byte Ethernet header
        iph = struct.unpack("!BBHHHBBH4s4s", packet[14:34])

        total_length = iph[2]
        ttl = iph[5]
        protocol = iph[6]

        src_ip = socket.inet_ntoa(iph[8])
        dst_ip = socket.inet_ntoa(iph[9])

        print("\n-----------------------------")
        print("Source IP      :", src_ip)
        print("Destination IP :", dst_ip)
        print("Protocol       :", protocol)
        print("Packet Length  :", total_length)
        print("TTL            :", ttl)

except KeyboardInterrupt:
    print("\nPacket capture stopped.")

finally:
    sock.close()
