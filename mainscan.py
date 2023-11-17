import sys
import arp
import icmp
from colorama import Fore, Style
from model import parse_arguments

import sys

if (len(sys.argv)) == 1:
    sys.exit("Too few arguments")

parsed_args = parse_arguments()
print(parsed_args)

'''if len(sys.argv) == 3 and (sys.argv[1] == "-a" or sys.argv[1] == "--arp") or (sys.argv[1] == "-i" or sys.argv[1] == "--icmp"):
    ip_argument = sys.argv[2]
    result = parse_arguments(ip_argument)
    print(result)
else:
    print("Usage: python main.py -a <ip_argument>")
'''
##print(str(sys.argv[2]))

# ARP scan
if parsed_args['scan_type'] == 'a':
    arp.art(parsed_args)

# ICMP scan
elif parsed_args['scan_type'] == 'i':
    icmp.ic(parsed_args)



'''
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
   
'''
