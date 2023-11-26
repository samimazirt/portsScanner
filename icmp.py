from colorama import Fore, Back, Style
from scapy.all import *
from scapy.layers.inet import ICMP, IP

import logging
import subprocess

def ic(model):
    toprint = "\n"

    for address in model['ip']:
        #sr = send and receive, on envoie un paquet au peripherique, si b est nul, l'adresse est live. car reponse
        #contient les paquets avec une reponse, et b ceux sans réponse
        reponse, b = sr(IP(dst=str(address))/ICMP(), timeout=3, verbose=1)
        if not b:
                toprint += f" {address} {Fore.GREEN} is LIVE{Style.RESET_ALL}.\n"
        else:
             toprint += f" {address} {Fore.RED} is NOT LIVE{Style.RESET_ALL}.\n"

    print("\n\n\n")
    print(f"----------ICMP Scan Results----------\n")
    logging.info(toprint)
