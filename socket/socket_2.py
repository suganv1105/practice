import socket
ipaddress=socket.gethostbyname('www.google.com')
print(ipaddress)
hostname=socket.gethostbyaddr(ipaddress)
print(hostname)

# An example script to connect to Google using socket
# programming in Python
import socket # for socket