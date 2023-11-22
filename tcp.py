import subprocess
from colorama import Fore, Back, Style
from scapy.all import *
from scapy.layers.inet import ICMP, IP
import logging
from socket import *
import sys
import socket
from socket import getservbyname, getservbyport
from model import parse_arguments



def sc(i,j):
    host = i
    ports = int(j)

    trg = socket.gethostbyname(host)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    st = s.connect_ex((trg,ports))
    
# On essaie de se connecter à un port, si la reponse est 0 le port est ouvert
    if st == 0:
        print("Port " + str(ports) + ":" + Fore.GREEN + " OPENED".format(ports) + Style.RESET_ALL)
        #We use 'try', so if there is a service behind an opened port, we display it,and if not, there aren't any error
    else:
         print("Port " + str(ports) + ":" + Fore.RED + " CLOSED".format(ports) + Style.RESET_ALL)
    try:
            #On précise le protocole derrière le port
        name = socket.getservbyport(ports, "tcp")
        print("Service: " + name)
    except:
        print(Fore.YELLOW + "No service found for the " + " port " + str(ports) + Style.RESET_ALL)
    s.close()
    print ("\n")

def tc(scan_info):
    host = scan_info['ip']
    ports = scan_info['ports']
    for i in host:
        print("\nIP ADDRESS: " + str(i))
        for j in ports:
            sc(i,j)

