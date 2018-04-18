import socket
import Test
import packets

UDP_IP = "127.0.0.1"
UDP_PORT = 8080
MESSAGE = "Dexter says hai !"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

chunkSize = 500
count = 0
ChunksNo = Test.splitFile('image.jpeg', chunkSize)

for i in range(0, ChunksNo, 1):
    chunkNum = i * chunkSize
    count += 1
    chunkName = 'chunk' + '%s' % chunkNum
    f = open(chunkName, 'rb')
    p = packets.dataPacket(count, f.read())

    s.sendto(str(p), (UDP_IP, UDP_PORT))

s.close()
