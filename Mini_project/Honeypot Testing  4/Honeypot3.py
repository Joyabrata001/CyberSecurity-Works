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
    try:
        data = conn.recv(1024)
        if not data: break
        data_str = data.decode("utf-8")

        # Extract the User-Agent header from the incoming HTTP request
        if "User-Agent" in data_str:
            user_agent = data_str.split("User-Agent:")[1].split("\r\n")[0]
            print("User-Agent:", user_agent)
        print("Received data:", data_str)
    except:
        # Handle exceptions, such as when the connection is closed by the client
        print("Connection closed by client")
        break

conn.close()