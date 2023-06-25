import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the honeypot
server_address = ('0.0.0.0', 5000)
print('Connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send a message to the honeypot
    message = b'Message'
    print('Sending: ', message)
    sock.sendall(message)

    # Receive the response from the honeypot
    data = sock.recv(16)
    print('Received: ', data)
finally:
    # Clean up the connection
    sock.close()