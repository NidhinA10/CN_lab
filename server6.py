import socket
from datetime import datetime

PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', PORT))

print("=====================================")
print(" UDP Time Server Started")
print(" Listening on Port", PORT)
print("=====================================")

while True:
    data, addr = server.recvfrom(1024)

    current_time = datetime.now().strftime("%a %b %d %H:%M:%S %Y")

    server.sendto(current_time.encode(), addr)

    print("Time request served.")
