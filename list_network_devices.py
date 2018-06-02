
import nmap

def list_network_devices(base_ip, netmask_bits, info=['name']):
    #TODO: verify input

    nm = nmap.PortScanner()
    nm.scan(hosts='{}/{}'.format(base_ip, netmask_bits), arguments='-sn -PS22,3389')
    host_list = [(ip, nm[ip]['hostnames'][0]['name']) for ip in nm.all_hosts()]
    return host_list

