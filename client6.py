import socket

PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ('127.0.0.1', PORT)

client.sendto("TIME".encode(), server_addr)

data, addr = client.recvfrom(1024)

print("\nCurrent Server Time")
print(data.decode())

client.close()
