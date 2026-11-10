import socket

PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sentence = input("Enter sentence:\n")

client.sendto(sentence.encode(), ('127.0.0.1', PORT))

data, addr = client.recvfrom(1024)

print("\nTranslated Sentence:")
print(data.decode())

client.close()
