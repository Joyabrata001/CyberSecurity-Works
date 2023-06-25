#EMULATING SSH SERVICE(NOT WORKING!!!!!!!!!!)

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

        # Emulate an SSH service
        client_socket.sendall(b'SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n')
        while True:
            #data = client_socket.recv(1024).decode()
            #data = client_socket.recv(1024).decode("ISO-8859-1")
            try:
                data = client_socket.recv(1024).decode("UTF-8")
            except UnicodeDecodeError:
                continue


            if not data:
                break
            if data.startswith('SSH'):
                client_socket.sendall(b'SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n')
            elif data.startswith('USER'):
                client_socket.sendall(b'\r\n')
            elif data.startswith('QUIT'):
                client_socket.sendall(b'\r\n')
                break
            else:
                client_socket.sendall(b'\r\n')

        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    honeypot_server()