from colorama import Fore, Back, Style
from socket import *
import sys
import socket



def dc(host,ports):
    MESSAGE = "Ping test"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    socket.setdefaulttimeout(1)

    if s == -1:
        print("socket creation failed")
    so = socket.socket(AF_INET,SOCK_RAW,IPPROTO_ICMP)
    if so == -1:
        print("icmp creation failed")

    opened = False
    try:
        s.sendto(MESSAGE.encode('utf_8'), (host, ports))
        so.settimeout(1)
        data, addr = so.recvfrom(1024)
    except timeout:
        try:
            se = socket.getservbyport(ports, 'udp')
            if not se:
                pass
            else:
                opened = True
                print("\nPort " + str(ports) + ":" + Fore.GREEN + " OPENED".format(ports) + Style.RESET_ALL)
                try:
                    name = socket.getservbyport(ports, "udp")
                    print("Service: " + name)
                except:
                    print(Fore.YELLOW + "No service found for the " + str(ports) + " port")
                    print(Style.RESET_ALL)
        except:
            pass

    except error as sock_err:
        if (sock_err.errno == sock_err.errno.ECONNREFUSED):
            print(sock_err("Connection refused"))
        s.close()
        so.close()

    if opened == False:
        print("\nPort " + str(ports) + ":" + Fore.RED + " CLOSED".format(ports) + Style.RESET_ALL)
        try:
            name = socket.getservbyport(ports, "udp")
            print("Service: " + name)
        except:
            print(Fore.YELLOW + "No service found for the " + str(ports) + " port")
            print(Style.RESET_ALL)

 


    
def ud(n, typ, ports):
    if typ == 1:
        print("\n--------------------IP Address: " + str(n) + " ---------------------------")
        for i in ports:
            dc(n,int(i))

    if typ == 2:
        i = 0
        deb = ""
        while n[i] != '/':
            deb+=n[i]
            i += 1
        l = len(n) - 1
        fin = ""
        v = i + 1
        while v < l + 1:
            fin += n[v]
            v += 1
        while n[i] != '.':
            i -= 1
        i += 1
        mid = ""
        o = 0
        address = ""
        while o < i:
            address += n[o]
            o += 1
        while n[i] != '/':
            mid += n[i]
            i += 1
        mid1 = int(mid)
        fin1 = int(fin)
        for i in range(mid1, fin1 + 1):
            add = address + str(i)
            print("\n--------------------IP Address: " + add + " ---------------------------")
            for ii in ports:
                dc(add,int(ii))   
