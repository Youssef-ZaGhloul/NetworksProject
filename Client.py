import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8080
MESSAGE = "Dexter says hai !"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

modifiedMessage, serverAddress = s.recvfrom(2048)

print(modifiedMessage.decode())

s.close()