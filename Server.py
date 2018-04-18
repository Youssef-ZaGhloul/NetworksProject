import socket
UDP_PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', UDP_PORT))

while True:
    message, ClientAddress = s.recvfrom(500)
    print ClientAddress
    print message