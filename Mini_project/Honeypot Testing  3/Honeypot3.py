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

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        # Emulate a Telnet service
        username = None
        password = None

        client_socket.sendall(b'\nlogin: ')
        data = client_socket.recv(1024).strip()
        if data:
            username = data

        if username:
            client_socket.sendall(b'\nPassword: ')
            data = client_socket.recv(1024).strip()
            if data:
                password = data

        if username and password:
            client_socket.sendall(b'Access granted!\r\n')
        else:
            client_socket.sendall(b'Access denied!\r\n')

        client_socket.sendall(b'Hello World')

        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    honeypot_server()