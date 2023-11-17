import sys
from scapy.all import *
import requests
import time
from scapy.layers.l2 import ARP, Ether, srp



def art(n):
    print("\n*************** ARP SCAN ***************\n")

    for add in n['ip']:
        request = ARP()
        request.pdst = add

        broadcast = Ether()
        broadcast.dst = 'ff:ff:ff:ff:ff:ff'

        request_broadcast = broadcast / request
        clients = srp(request_broadcast, timeout=1, verbose=False)[0]

        url = "https://api.macvendors.com/"
        for i in clients:
            print("\n")
            time.sleep(1)
            print(i[1].psrc + "      " + i[1].hwsrc)

            response = requests.get(url + i[1].hwsrc)
            r = response.content.decode()
            print(response.content.decode())
