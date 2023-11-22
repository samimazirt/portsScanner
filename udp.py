import socket
from colorama import Fore, Back, Style
from model import parse_arguments

def ud(scan_info):
    ip = scan_info['ip'][0]
    ports = scan_info['ports']

    open_ports = []
    closed_ports = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            sock.sendto(b'', (ip, int(port)))
            data, addr = sock.recvfrom(1024)
            open_ports.append(port)
            print(f"Port {port}/UDP on {ip} is open.")
        except socket.timeout:
            closed_ports.append(port)
            print(f"Port {port}/UDP on {ip} is closed.")
        finally:
            sock.close()
    print_results(ip, open_ports, closed_ports)

def print_results(ip, open_ports, closed_ports):
    print(f"\nUDP Scan Results for {ip}:")

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"  {port}/UDP is open.")

    if closed_ports:
        print("Closed ports:")
        for port in closed_ports:
            print(f"  {port}/UDP is closed.")
