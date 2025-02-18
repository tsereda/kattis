import re

ip = input()

if re.match(r".+\..+\..+\..+", ip):
    ipv4 = '.'.join(list(reversed(ip.split(".")))) + '.in-addr.arpa.'
    print(ipv4) 
else:
    while ip.count(':') < 7:
        ip = ''.join((':', ip))
    for char, i in ip:
        if char == ':' and ip[:i].contain(':'):
            
    print(ip)
    ipv6 = '.'.join(list(reversed(ip.replace(':', '')))) + '.ip6.arpa.'
    print(ipv6)