import argparse
import ipaddress

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

    # port list to return
    ports_list = []

    if ',' in ports_arg:
        ports_list = ports_arg.split(',')
    elif '-' in ports_arg:
        parts = ports_arg.split('-')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            ports_list = list(map(str, range(int(parts[0]), int(parts[1]) + 1)))
        else:
            raise ValueError('Invalid port range format')
    else:
        ports_list.append(ports_arg)

    return ports_list
