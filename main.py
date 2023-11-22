import socket
import time

def scan_ports(start_port, end_port):
    open_ports = []

    target_ip = socket.gethostbyname(socket.gethostname())
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    end_time = time.time()
    scan_time = end_time - start_time

    return open_ports, scan_time

def get_service_name(port, protocol="tcp"):
    try:
        service_name = socket.getservbyport(port, protocol)
        return service_name
    except socket.error:
        return "Unknown"

def main():
    start_port = 1  # Начальный порт
    end_port = 1024  # Конечный порт

    print(f"Начало сканирования портов на {socket.gethostname()} ({socket.gethostbyname(socket.gethostname())})...")
    open_ports, scan_time = scan_ports(start_port, end_port)

    if open_ports:
        print("Открытые порты:")
        for port in open_ports:
            service_name = get_service_name(port)
            print(f"Порт {port} ({service_name}): открыт")
    else:
        print("Открытых портов не обнаружено.")

    print(f"Время сканирования: {scan_time:.2f} секунд")

if name == "main":
    main()
