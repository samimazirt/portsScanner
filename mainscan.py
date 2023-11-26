from colorama import Fore, Style
from model import parse_arguments

import sys
import arp
import icmp
import udp
import tcp
import sys

if (len(sys.argv)) == 1:
    sys.exit("Not enough arguments")

parsed_args = parse_arguments()
# print(parsed_args)

# ARP scan
if parsed_args['scan_type'] == 'a':
    arp.art(parsed_args)

# ICMP scan
elif parsed_args['scan_type'] == 'i':
    icmp.ic(parsed_args)

#UDP scan
elif parsed_args['scan_type'] == 'u':
    udp.ud(parsed_args)

#TCP scan
elif parsed_args['scan_type'] == 't':
    tcp.tc(parsed_args)

else:
    sys.exit(1)
