from colorama import Fore, Style
from scapy.all import *
import logging

def ud(model):

    #recup IP et des ports
    ip = model['ip'][0]
    ports = model['ports']

    open_ports = []
    closed_ports = []

    toprint = f"\nIP ADDRESS: {str(ip)}\n"

    for port in ports:
        int_port = int(port)
        # UDP packet
        packet = IP(dst=ip) / UDP(dport=int_port)

        try:
            # envoi du packet et attente de la réponse
            response = sr1(packet, timeout=1, verbose=False)

            # vérifie si réponse
            if response and response.haslayer(UDP):
                open_ports.append(int_port)
                toprint += f"\nPort {int_port} is {Fore.GREEN}OPENED{Style.RESET_ALL}.\n"
            else:
                closed_ports.append(int_port)
                toprint += f"\nPort {int_port} is {Fore.RED}CLOSED{Style.RESET_ALL}.\n"

        # toutes exception = port fermé
        except Exception as e:
            closed_ports.append(int_port)
            toprint += f"\nPort {int_port} is {Fore.RED}CLOSED{Style.RESET_ALL}.\n"

    print("\n\n\n")
    print(f"----------UDP Scan Results----------\n")
    logging.info(toprint)
