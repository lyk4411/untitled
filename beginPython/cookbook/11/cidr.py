

import ipaddress
net = ipaddress.ip_network('123.45.67.64/27')
print(net)
print('=============================')
for a in net:
    print(a)