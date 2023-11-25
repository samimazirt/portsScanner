from colorama import Fore, Style
import logging
from scapy.all import *

def sc(i, j, toprint):
    host = i
    port = int(j)

    # on construit le TCP SYN packet
    packet = IP(dst=host) / TCP(dport=port, flags='S')

    # envoi du packet et attente de la réponse
    response = sr1(packet, timeout=1, verbose=False)

    # vérifie si réponse
    if response and response.haslayer(TCP):
        # vérifie si le flag tcp indique un port ouvert
        if response[TCP].flags == 18:  # 18 => SYN-ACK
            toprint += f"Port {port} is {Fore.GREEN}OPENED{Style.RESET_ALL}.\n"
        else:
            toprint += f"Port {port} is {Fore.RED}CLOSED{Style.RESET_ALL}.\n"
    else:
        toprint += f"Port {port} is {Fore.RED}CLOSED{Style.RESET_ALL}.\n"

    # récupère service
    try:
        name = socket.getservbyport(port, "tcp")
        toprint += f"Service: {name}\n"
    except:
        toprint += f"{Fore.YELLOW}No service found for port {port}{Style.RESET_ALL}.\n"

    return toprint

def tc(model):
    hosts = model['ip']
    ports = model['ports']
    toprint = ""

    for host in hosts:
        toprint += f"\nIP ADDRESS: {str(host)}\n\n"
        for port in ports:
            toprint = sc(host, port, toprint)
            toprint += '\n'

    print("\n\n\n")
    print(f"----------TCP Scan Results----------\n")
    logging.info(toprint)
