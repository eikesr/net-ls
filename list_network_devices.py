
import ipaddress
import nmap

def list_network_devices(base_ip, netmask_bits, info=['name']):
    # validate input
    ipaddress.IPv4Address(base_ip)
    if not(isinstance(netmask_bits, int) and netmask_bits <= 32 and netmask_bits >= 0):
        raise ValueError('netmask_bits invalid')

    nm = nmap.PortScanner()
    nm.scan(hosts='{}/{}'.format(base_ip, netmask_bits), arguments='-sn -PS22,3389')

    results = [nm.all_hosts()]

    if 'name' in info:
        hostnames = [nm[ip]['hostnames'][0]['name'] for ip in nm.all_hosts()]
        results.append(hostnames)

    if 'state' in info:
        states = [nm[ip]['status']['state'] for ip in nm.all_hosts()]
        results.append(states)

    return list(zip(*results))

