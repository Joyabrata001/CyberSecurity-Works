import socket

host = ''  # Listen on all available interfaces
port = 80  # Port number to use

s = socket.socket()
s.bind((host, port))
s.listen(1)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("The IP address of the honeypot is:", IPAddr)

print("Listening on port", port)

conn, addr = s.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data: break
    print("Received data:", data)

conn.close()