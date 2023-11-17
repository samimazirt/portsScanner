import subprocess
from colorama import Fore, Back, Style
from scapy.all import *
from scapy.layers.inet import ICMP, IP



def ic(ip_list):
    toprint = ""

    for address in ip_list['ip']:
        '''print("\n\n SCANNING... Please Wait \n\n")
        res = subprocess.call(['ping', '-c', '3', address])
        if res == 0:
            toprint += f" {address} {Fore.GREEN}is LIVE\n{Style.RESET_ALL}"
        else:
            toprint += f" {address} {Fore.RED}is NOT LIVE\n{Style.RESET_ALL}"'''
        reponse, b = sr(IP(dst=str(address))/ICMP(), timeout=3, verbose=1)
        if reponse == False:
                toprint += f" {address} {Fore.GREEN}is LIVE\n{Style.RESET_ALL}"

        else:
                toprint += f" {address} {Fore.RED}is NOT LIVE\n{Style.RESET_ALL}"


    print("\n\n\n")
    print("----------ICMP Scan Results----------\n\n")
    print(toprint)
