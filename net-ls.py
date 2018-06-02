#!/usr/bin/env python3

import list_network_devices as lsn

def main():
    network_devices = lsn.list_network_devices('192.168.1.0', 24)
    print(network_devices)

if __name__ == "__main__":
    main()

