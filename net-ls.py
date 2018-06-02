#!/usr/bin/env python3

import list_network_devices as lsn
import argparse

def main(ip, netmask_bits):
    network_devices = lsn.list_network_devices(ip, netmask_bits)
    print(network_devices)

if __name__ == "__main__":
    parser = argparse.ArgumentParser('List IP and hostname of devices in the network')
    parser.add_argument('ip', type=str, help='IPv4 base address of the network (e.g., 192.168.0.0)')
    parser.add_argument('--netmask_bits', default=24, type=int, required=False, help='Number of bits of the netmask. For local networks typically 24.')

    args = parser.parse_args()
    main(args.ip, args.netmask_bits)

