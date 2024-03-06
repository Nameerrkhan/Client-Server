import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

while True:
    message = input("Enter your message: ")
    s.send(message.encode())
    if message.lower() == "bye":
        break
    reply = s.recv(1024).decode()
    print(f"Received: {reply}")

s
