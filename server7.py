import socket
import os

PORT = 9000
BUFFER_SIZE = 2048

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', PORT))

print("====================================")
print(" UDP Concurrent File Server Started")
print(" Listening on Port", PORT)
print("====================================")

while True:
    data, client_addr = server.recvfrom(1024)
    filename = data.decode().strip()

    pid = os.fork()

    if pid == 0:
        # Child process
        try:
            with open(filename, "r") as file:
                contents = file.read()

            response = f"Handled by Server PID : {os.getpid()}\n\n"
            response += contents

        except FileNotFoundError:
            response = f"Handled by Server PID : {os.getpid()}\n\n"
            response += "Requested File Not Found."

        server.sendto(response.encode(), client_addr)

        print(f"Request for {filename} served by PID {os.getpid()}")

        os._exit(0)

    # Parent continues waiting for the next client
