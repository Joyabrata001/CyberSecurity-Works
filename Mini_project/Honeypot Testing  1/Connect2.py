import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('14.139.223.166', 12345)
print('Connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data to the server
    message = 'Hello, server!'
    print('Sending data: ', message)
    sock.sendall(message.encode())

    # Receive data from the server
    data = sock.recv(16)
    print('Received data: ', data.decode())

finally:
    # Clean up the socket
    print('Closing the socket')
    sock.close()