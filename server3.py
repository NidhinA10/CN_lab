
import socket

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket
server.bind(('127.0.0.1', 12345))

print("UDP Server is running...")

# Receive message
data, addr = server.recvfrom(1024)
print("Client:", data.decode())

# Send response
msg = "Hello from UDP server"
server.sendto(msg.encode(), addr)

server.close()

