import socket
from colorama import Fore, Back, Style
from model import parse_arguments

def ud(scan_info):
    ip = scan_info['ip'][0]
    ports = scan_info['ports']
    #recup d'IP et des ports

    open_ports = []
    closed_ports = []
    #
    for port in ports:
        try:
            #on cree u socket de type DGRAM, c'est ce type qui est utilisé dans UDP
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #attente d'1 seconde
            sock.settimeout(1)
            #envoi du message
            sock.sendto(b'', (ip, int(port)))
            data, addr = sock.recvfrom(1024)
            #si aucune exeption n'est trigger, cela signifie que les données ont bien été recues
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
