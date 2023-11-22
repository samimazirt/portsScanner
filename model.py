import argparse
import ipaddress
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_valid_ports(ports):
    try:
        port_list = [int(port) for port in ports.split(',')]
        for port in port_list:
            if not (0 < port < 65536):
                return False
        return True
    except ValueError:
        return False


def parse_ip_arg(ip_arg):
    # initialize ip list to return
    ip_list = []
     
    if ',' in ip_arg:
        ip_list = ip_arg.split(',')
    elif '/' in ip_arg:
        # CIDR notation
        ip_list = [str(ip) for ip in ipaddress.IPv4Network(ip_arg, strict=False)]
    elif '-' in ip_arg:
        start_ip, end_ip = ip_arg.split('-')

        # create a list of ip addresses in the range
        start_ip_obj = ipaddress.IPv4Address(start_ip)
        end_ip_obj = ipaddress.IPv4Address(end_ip)

        while start_ip_obj <= end_ip_obj:
            ip_list.append(str(start_ip_obj))
            start_ip_obj += 1
    else:
        ip_list.append(ip_arg)
    
    for i in ip_list: #check si chaque element de la liste est bien une ip
        if not is_valid_ip(i):
            logging.error('Not valid IP')
            sys.exit(1)  

    return ip_list

def parse_arguments():
    parser = argparse.ArgumentParser(description='Port Scanner')

    # scan type parsing
    parser.add_argument('-x', '--scan-type', required=True, choices=['a', 'i', 'u', 't'], help='Specify scan type (a, i, u, t)')
    # ip address
    parser.add_argument('-ip', '--ip', required=True, help='Input IP address, IP range, or CIDR notation')
    # port if needed
    parser.add_argument('-p', '--ports', help='Specify ports to scan')

    args = parser.parse_args()
    return {
        'scan_type': args.scan_type,
        'ip': parse_ip_arg(args.ip),
        'ports': parse_ports_arg(args.ports)
    }

def parse_ports_arg(ports_arg):
    # if no port Specified, return none
    if not ports_arg:
        return None
    if not is_valid_ports(ports_arg):
        logging.error('Not valid ports')
        sys.exit(1)    
    # port list to return
    ports_list = []

    if ',' in ports_arg:
        ports_list = ports_arg.split(',')
    elif '-' in ports_arg:
        parts = ports_arg.split('-')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            ports_list = list(map(str, range(int(parts[0]), int(parts[1]) + 1)))
        else:
            logging.error('Invalid port range format')
    else:
        ports_list.append(ports_arg)

    return ports_list
