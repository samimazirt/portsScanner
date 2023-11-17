import sys
from scapy.all import *
import requests
import time




def art(n):
    print("\n*************** ARP SCAN ***************\n")
    

    request = scapy.ARP()
  

    request.pdst = n


    broadcast = scapy.Ether()
  
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
    
    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 1, verbose = False)[0]
    
    url = "https://api.macvendors.com/"
    #Print IP and MAC addresses
    for i in clients:
        #We delay the execution of our function so the API doesn't display us an error message
        print("\n")
        time.sleep(1)
        print(i[1].psrc + "      " + i[1].hwsrc)
        #We use the API of MAC Vendors to get the manufactures name

        #We use get method to fetch details of the MAC address
        
            
        response = requests.get(url+ i[1].hwsrc)
        r = response.content.decode()
        print(response.content.decode())
        
