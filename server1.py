import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.0.0.1',12345))

server.listen(5)
print("Server Listening...")

conn,addr = server.accept()
print("Connected to : ",addr)

data = conn.recv(1024).decode()
print("Client :",data)

conn.send("Hello from server".encode())

conn.close()
server.close()

