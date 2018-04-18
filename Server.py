import socket

UDP_PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', UDP_PORT))

while True:
    message, ClientAddress = s.recvfrom(2048)
    print ClientAddress
    modifiedMessage = message.decode()
    s.sendto(modifiedMessage.encode(), ClientAddress)
    print "received message:", message
