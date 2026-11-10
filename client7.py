import socket

PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter File Name : ")

client.sendto(filename.encode(), ('127.0.0.1', PORT))

data, addr = client.recvfrom(2048)

print("\n=====================================")
print("Response Received From Server")
print("=====================================\n")

print(data.decode())

client.close()
