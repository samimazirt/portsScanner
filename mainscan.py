import sys
import arp
import icmp
from colorama import Fore, Style


if (len(sys.argv)) == 1:
    sys.exit("Too few arguments")




if ((sys.argv[1]) == "-a" or (sys.argv[1]) == "--arp") and len(sys.argv) == 3:
    r = sys.argv[2]

    le = len(r)
    i = 0

    sep = ""
    while i < le:
        if r[i] == '/' or r[i] == '-':
            
            if r[i] == '-':
                sep = 'tir'
            elif r[i] == '/':
                sep = "sla"
        i+= 1
    if sep == "tir":
        i = le - 1
        while r[i] != '.':
            i -= 1
        num = ""
        i += 1
        e = i
        while i < le:
            num += r[i]
            i += 1
        i = 0
        ad = ""
        while r[i] != '-':
            ad += r[i]
            i += 1
        ad += '/'
        ad += num
        r = ad
 
    arp.art(r)



elif ((sys.argv[1]) == "-i" or (sys.argv[1]) == "--icmp") and len(sys.argv) == 3:
    r = sys.argv[2]
    le = len(r)
    i = 0
    typ = 1
    sep = ""
    while i < le:
        if r[i] == '/' or r[i] == '-':
            typ = 2
            if r[i] == '-':
                sep = 'tir'
            elif r[i] == '/':
                sep = "sla"
        i+= 1
    if typ == 2 and sep == "tir":
        i = le - 1
        while r[i] != '.':
            i -= 1
        num = ""
        i += 1
        e = i
        while i < le:
            num += r[i]
            i += 1
        i = 0
        ad = ""
        while r[i] != '-':
            ad += r[i]
            i += 1
        ad += '/'
        ad += num
        r = ad
    icmp.ic(r, typ)   




elif ((sys.argv[1]) == "-t" or (sys.argv[1]) == "--tcp") and (len(sys.argv) == 3 or len(sys.argv) == 5):
    print("tcp")




elif ((sys.argv[1]) == "-u" or (sys.argv[1]) == "--udp") and (len(sys.argv) == 3 or len(sys.argv) == 5):
    print("udp")

else:
    print(Fore.RED + "\n\n-----------INVALID Command----------\n" + Style.RESET_ALL)
    
    print(Fore.GREEN + "\n-----------ARP Scan help------------\n" + Style.RESET_ALL)
    print(Fore.YELLOW + " - For ARP scan of x.x.x.x IP address:\n" + Style.RESET_ALL)
    print("python3 main.py -a x.x.x.x OR python3 project.py --arp x.x.x.x\n")
    print(Fore.YELLOW + " - For ARP scan of a range of IP addresses:\n" + Style.RESET_ALL)
    print("python3 main.py -a x.x.x.x/x OR python3 project.py -a x.x.x.x-x.x.x.x \n\n\n")  
    
    print(Fore.GREEN + "-----------ICMP Scan help-------------\n"+ Style.RESET_ALL )
    print(Fore.YELLOW + " - For ICMP scan of x.x.x.x IP address:\n"+ Style.RESET_ALL )
    print("python3 main.py -i x.x.x.x OR python3 project.py --icmp x.x.x.x\n"+ Style.RESET_ALL )
    print(Fore.YELLOW + " - For ICMP scan of a range of IP addresses:\n"+ Style.RESET_ALL )
    print("python3 main.py -i x.x.x.x/x OR python3 project.py -i x.x.x.x-x.x.x.x\n\n\n")
   
