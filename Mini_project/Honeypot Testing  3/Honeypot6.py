#EMULATING SMTP SERVICE(NOT WORKING!!!!!!!!!!)

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

        # Emulate an SMTP service
        client_socket.sendall(b'220 SMTP Server Ready\r\n')
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            if data.startswith('HELO'):
                client_socket.sendall(b'250 Hello\r\n')
            elif data.startswith('MAIL FROM'):
                client_socket.sendall(b'250 OK\r\n')
            elif data.startswith('RCPT TO'):
                client_socket.sendall(b'250 OK\r\n')
            elif data.startswith('DATA'):
                client_socket.sendall(b'354 End data with <CR><LF>.<CR><LF>\r\n')
            elif data.startswith('QUIT'):
                client_socket.sendall(b'221 Bye\r\n')
                break
            else:
                client_socket.sendall(b'500 Unknown command\r\n')

        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    honeypot_server()
