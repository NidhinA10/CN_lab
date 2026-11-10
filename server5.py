
import socket
import threading

PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', PORT))
server.listen()

clients = []

print("Chat Server Started...")


def broadcast(message, sender):
    for c in clients:
        if c != sender:
            try:
                c.sendall(message)
            except:
                pass


def handle_client(conn):
    name = conn.recv(1024).decode()
    clients.append(conn)

    print(name, "connected")

    while True:
        try:
            msg = conn.recv(1024).decode()

            if not msg or msg.lower() == "exit":
                break

            print(name, ":", msg)
            broadcast((name + " : " + msg).encode(), conn)

        except:
            break

    if conn in clients:
        clients.remove(conn)

    print(name, "disconnected")
    conn.close()


try:
    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn,), daemon=True)
        t.start()

except KeyboardInterrupt:
    print("\nServer shutting down...")

    for c in clients:
        c.close()

    server.close()
    print("Server closed.")

