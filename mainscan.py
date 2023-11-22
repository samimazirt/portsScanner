import sys
import arp
import icmp
import udp
import tcp
from colorama import Fore, Style
from model import parse_arguments

import sys

if (len(sys.argv)) == 1:
    sys.exit("Too few arguments")
    

parsed_args = parse_arguments()
print(parsed_args)

# ARP scan
if parsed_args['scan_type'] == 'a':
    arp.art(parsed_args)

# ICMP scan
elif parsed_args['scan_type'] == 'i':
    icmp.ic(parsed_args)

elif parsed_args['scan_type'] == 'u':
    udp.ud(parsed_args)
elif parsed_args['scan_type'] == 't':
    tcp.tc(parsed_args)
'''

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
   
'''
