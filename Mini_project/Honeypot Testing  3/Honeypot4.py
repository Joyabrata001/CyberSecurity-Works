#EMULATING TELNET SERVICE

import socket

def honeypot_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Honeypot listening on {}:{}'.format(*server_address))

    # Store valid credentials
    valid_credentials = [
        ('user1', 'password1'),
        ('user2', 'password2'),
        ('user3', 'password3'),
    ]

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        # Emulate a Telnet service
        username = None
        password = None

        client_socket.sendall(b'login: ')
        data = b''
        while not data.endswith(b'\r\n'):
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            data += chunk
        username = data.strip().decode()

        if username:
            client_socket.sendall(b'Password: ')
            data = b''
            while not data.endswith(b'\r\n'):
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                data += chunk
            password = data.strip().decode()

        if (username, password) in valid_credentials:
            client_socket.sendall(b'Access granted!\r\n')
        else:
            client_socket.sendall(b'Access denied!\r\n')

        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    honeypot_server()