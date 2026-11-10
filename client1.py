import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",12345))

client.send("Hello from client".encode())

data = client.recv(1024).decode()
print("Server :",data)

client.close()
