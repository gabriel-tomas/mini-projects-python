from ipaddress import ip_address
import socket

ip = socket.gethostbyname("www.google.com")

print(ip)