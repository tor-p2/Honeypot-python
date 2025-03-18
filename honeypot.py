import socket
import threading
import datetime

# Honeypot configuration
HOST = "0.0.0.0"  # Listening in all interfaces 
PORT = 2222       # Honeypot port
LOG_FILE = "honeypot_log.txt"

def log_attempt(ip, data):
    """Save attempts of connections in a file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] attempt from {ip}: {data.strip()}\n")
    print(f"[!] registered: {ip} -> {data.strip()}")

def handle_connection(client_socket, client_address):
    """New connection incoming"""
    ip, port = client_address
    print(f"[+] Connection detected from {ip}:{port}")

    # Fake welcome message
    fake_banner = "Welcome to Secure SSH v2.0\nUser: "
    client_socket.send(fake_banner.encode())

    # Fake login
    try:
        data = client_socket.recv(1024).decode().strip()
        log_attempt(ip, data)
    except Exception as e:
        print(f"[ERROR] Problem with {ip}: {e}")

    # Close conection
    client_socket.close()

def start_honeypot():
    """Start honeypot and listening connections"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[LISTENING] Honeypot active in {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_connection, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_honeypot()
