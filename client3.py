
import socket

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
addr = ('127.0.0.1', 12345)

# Send message
msg = "Hello from UDP client"
client.sendto(msg.encode(), addr)

# Receive response
data, addr = client.recvfrom(1024)
print("Server:", data.decode())

client.close()

