import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received message: {data}")
        reply = input("Enter your reply: ")
        conn.send(reply.encode())
    conn.close()
