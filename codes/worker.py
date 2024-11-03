import socket
from urllib.parse import urlparse, parse_qs
import argparse
import time
from datetime import datetime

# Set up command-line arguments
parser = argparse.ArgumentParser(description="Simple HTTP Server")
parser.add_argument('-H', '--host', default='0.0.0.0', help='Host to bind the server (default: 0.0.0.0)')
parser.add_argument('-P', '--port', type=int, default=80, help='Port to bind the server (default: 80)')
args = parser.parse_args()

# Get HOST and PORT from arguments
HOST = args.host
PORT = args.port

# Create and bind socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"HTTP Server running on {HOST}:{PORT}...")

while True:
    try :
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        # print(f"Connected by {client_address}")

        # Receive the HTTP request from the client (usually the browser)
        request = client_socket.recv(1024).decode('utf-8')
        # print(f"Request from client:\n{request}")

        request_line = request.splitlines()[0] 
        url = request_line.split(' ')[1]      
        parsed_url = urlparse(url)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

       
        appID = ""

        if 'appID' in query_params:
            appID = query_params['appID'][0]
            # Prepare a simple HTTP response

            print(f"{datetime.now()} | Requested path: {path} | {appID}")
            body = ''
            if appID == 'long':
                time.sleep(5)
                body = f"Hello, World! appID = {appID} \nworker : {PORT}"

            elif appID == 'short':
                time.sleep(0.5)
                body = f"Hello, World! appID = {appID} \nworker : {PORT}"

            else :
                body = "unknown appID"

            content_length = len(body)

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {content_length}\r\n"
                "\r\n"
                f"{body}"
            )

            client_socket.sendall(response.encode('utf-8'))

    finally:
        client_socket.close()
