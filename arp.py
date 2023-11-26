from scapy.all import *
from scapy.layers.l2 import ARP, Ether, srp

import sys
import requests
import time

def art(model):
    toprint = ""
    for add in model['ip']:

        # création d'une requête ARP
        request = ARP()
        request.pdst = add

        # création d'un paquet Ethernet de diffusion
        broadcast = Ether()
        broadcast.dst = 'ff:ff:ff:ff:ff:ff'

        # construction requête ARP sur la couche Ethernet
        request_broadcast = broadcast / request

        # Envoi de la requête ARP et récupération des réponses
        clients = srp(request_broadcast, timeout=1, verbose=False)[0]

        # URL pour la recherche de l'adresse MAC
        url = "https://api.macvendors.com/"

        # ARP reçues
        for i in clients:
            toprint += "\n"
            time.sleep(1)
            toprint += f"{i[1].psrc}      {i[1].hwsrc}\n"
            # requête pour obtenir le nom du fournisseur de la carte réseau
            response = requests.get(url + i[1].hwsrc)
            toprint += response.content.decode() + "\n"

    print("\n\n\n")
    print(f"----------ARP Scan Results----------\n")
    logging.info(toprint)
