import socket
import random

PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', PORT))

N = int(input("Enter order of matrix (N): "))

matrix = [[random.randint(0, 50) for j in range(N)] for i in range(N)]

print("\nGenerated Matrix:")
for row in matrix:
    print(*row)

# Send N 
#client.send(str(N).encode())

# Send matrix
data = str(N)  + "\n" + str(matrix)+"\n"
client.send(data.encode())

# Receive result
result = client.recv(1024).decode()
print("\nMatrix Type:", result)

client.close()
