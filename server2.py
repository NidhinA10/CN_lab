import socket
import ast

PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', PORT))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()

# Receive N
file=conn.makefiel('r)
N = int(file.readline())

# Receive matrix
matrix = ast.literal_eval(file.readline())

upper = True
lower = True
diagonal = True

for i in range(N):
    for j in range(N):
        if i > j and matrix[i][j] != 0:
            upper = False

        if i < j and matrix[i][j] != 0:
            lower = False

        if i != j and matrix[i][j] != 0:
            diagonal = False

if diagonal:
    result = "Diagonal Matrix"
elif upper:
    result = "Upper Triangular Matrix"
elif lower:
    result = "Lower Triangular Matrix"
else:
    result = "Not a special matrix"

conn.send(result.encode())

conn.close()
server.close()
