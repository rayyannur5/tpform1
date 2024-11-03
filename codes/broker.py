import socket
import threading
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Simple HTTP Server")
parser.add_argument('-H', '--host', default='0.0.0.0', help='Host to bind the server (default: 0.0.0.0)')
parser.add_argument('-P', '--port', type=int, default=80, help='Port to bind the server (default: 80)')
args = parser.parse_args()

HOST = args.host
PORT = args.port

workers = [("localhost", 5001), ("localhost", 5002), ("localhost", 5003)]
request_count = [0, 0, 0] 
STRATEGY = "round_robin" 


def handle_client(client_conn, client_addr):
    try:
        client_data = client_conn.recv(1024)

        if STRATEGY == "even":
            worker_id = request_count.index(min(request_count))
        elif STRATEGY == "round_robin":
            worker_id = sum(request_count) % len(workers)

        worker_address = workers[worker_id]
        request_count[worker_id] += 1

        print(f"{datetime.now()}|{client_addr}\t|\t{worker_id}\t\t|\t{request_count}")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as worker_socket:
            worker_socket.connect(worker_address)
            worker_socket.sendall(client_data)
            response = worker_socket.recv(1024)
        
        client_conn.sendall(response)
    finally:
        client_conn.close()

# Initialize broker server on port 80
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as broker_socket:
    broker_socket.bind((HOST, PORT))
    broker_socket.listen()
    print(f"Broker server running on port {PORT}, waiting for browser requests...")
    print("time\t\t\t\t|\taddress\t\t\t|\tworker_id\t|\trequests/worker")

    while True:
        client_conn, client_addr = broker_socket.accept()
        threading.Thread(target=handle_client, args=(client_conn,client_addr)).start()
