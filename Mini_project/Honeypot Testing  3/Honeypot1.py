import socket
import time

def honeypot_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Honeypot listening on {}:{}'.format(*server_address))

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        # Emulate an FTP service
        client_socket.sendall(b'220 FTP Server Ready\r\n')
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            if data.startswith('USER'):
                client_socket.sendall(b'331 User name okay, need password\r\n')
            elif data.startswith('PASS'):
                client_socket.sendall(b'230 User logged in\r\n')
            elif data.startswith('QUIT'):
                client_socket.sendall(b'221 Goodbye\r\n')
                break
            elif data:
                client_socket.sendall(b'500 Unknown command\r\n')

        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    honeypot_server()