import socket
import threading
import datetime

# Configuración del Honeypot
HOST = "0.0.0.0"  # Escucha en todas las interfaces
PORT = 2222       # Puerto del honeypot (cambiar según necesidad)
LOG_FILE = "honeypot_log.txt"

def log_attempt(ip, data):
    """Registra intentos de conexión en un archivo"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] Intento desde {ip}: {data.strip()}\n")
    print(f"[!] Intento registrado: {ip} -> {data.strip()}")

def handle_connection(client_socket, client_address):
    """Maneja una nueva conexión entrante"""
    ip, port = client_address
    print(f"[+] Conexión detectada desde {ip}:{port}")

    # Mensaje de bienvenida falso para engañar al atacante
    fake_banner = "Bienvenido a Secure SSH v2.0\nUsuario: "
    client_socket.send(fake_banner.encode())

    # Recibir intento de usuario/contraseña (falso login)
    try:
        data = client_socket.recv(1024).decode().strip()
        log_attempt(ip, data)
    except Exception as e:
        print(f"[ERROR] Problema con {ip}: {e}")

    # Cerrar conexión
    client_socket.close()

def start_honeypot():
    """Inicia el honeypot y escucha conexiones"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[LISTENING] Honeypot activo en {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_connection, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_honeypot()