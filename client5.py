
import socket
import threading

PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', PORT))

name = input("Enter your name: ")
client.sendall(name.encode())

print("Connected to Chat Server")
print("Type exit to leave\n")


def receive():
    while True:
        try:
            msg = client.recv(1024).decode()

            if not msg:
                print("\nServer disconnected!")
                break

            print("\n" + msg)

        except:
            break


t = threading.Thread(target=receive, daemon=True)
t.start()

try:
    while True:
        message = input()

        if message.lower() == "exit":
            client.sendall(message.encode())
            break

        client.sendall(message.encode())

except (KeyboardInterrupt, EOFError):
    pass

finally:
    client.close()
    print("\nChat ended.")

