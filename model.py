import ipaddress

def parse_arguments(ip_arg):
    ip_list = []

    if ',' in ip_arg:
        ip_list = ip_arg.split(',')
    elif '-' in ip_arg:
        start_ip, end_ip = ip_arg.split('-')
        ip_range = list(map(str, ipaddress.IPv4Network(f"{start_ip}-{end_ip}", strict=False)))
        ip_list.extend(ip_range)
    else:
        ip_list.append(ip_arg)

    return {'ip': ip_list}
