import subprocess
from colorama import Fore, Back, Style
from scapy.all import *
from scapy.layers.inet import ICMP, IP

import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def ic(ip_list):
    toprint = ""

    for address in ip_list['ip']:
        #sr = send and receive, on envoie un paquet au peripherique, si b est nul, l'adresse est live. car reponse
        #contient les paquets avec une reponse, et b ceux sans réponse
        reponse, b = sr(IP(dst=str(address))/ICMP(), timeout=3, verbose=1)
        if not b:
                toprint += f" {address} {Fore.GREEN} is LIVE\n{Style.RESET_ALL}"
                
        else:
             toprint += f" {address} {Fore.RED} is NOT LIVE\n{Style.RESET_ALL}"
             
                


    print("\n\n\n")
    print("----------ICMP Scan Results----------\n\n")

    print(toprint)

