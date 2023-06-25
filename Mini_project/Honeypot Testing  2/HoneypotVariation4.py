import socket
import logging
import os
import datetime

def honeypot_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Honeypot listening on {}:{}'.format(*server_address))
    
    # Set up logging
    log_file = os.path.expanduser('~/Documents/Programming/Mini_project/Test2/honeypot.log')
    logging.basicConfig(filename=log_file, filemode='a',level=logging.INFO, format='%(asctime)s %(message)s')

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        # Receive and log the payload data
        payload = b''
        while True:
            chunk = client_socket.recv(4096)
            if chunk:
                payload += chunk
            else:
                break
        
        # Log the connection
        with open('honeypot.log', 'a') as log_file:
            logging.info('{} {} {}\n'.format(client_address, payload, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    honeypot_server()