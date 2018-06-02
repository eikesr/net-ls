# net-ls

Just a simple python function wrapping python-nmap to list all devices in a given network.
I did this as part of learning a bit about nmap, after becoming aware of its existence.

This could for example be useful if you want to display the devices currently in your home network.

### Setup

You need clone the repository and install python-nmap:
```
pip3 install python-nmap
```

You can run the small example application:
```
./net-ls.py <IPv4 of your home network>
```
which will print the IP addresses and host names of any device in your home network.

