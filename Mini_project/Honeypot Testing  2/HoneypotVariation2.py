import socket
import logging
import os
import time
import geoip2.database

def honeypot_server():
    # Load the GeoIP2 database
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')

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

        # Look up the source country
        response = reader.city(client_address[0])
        source_country = response.country.name
        
        # Log the connection
        #logging.info('{} - Connection from {}:{}'.format(time.ctime(), *client_address))
        # Log the connection information
        log_message = '[{}] Connection from {}:{} ({})'.format(
            time.strftime('%Y-%m-%d %H:%M:%S'),
            client_address[0], client_address[1], source_country)
        logging.info(log_message)
        
        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    honeypot_server()