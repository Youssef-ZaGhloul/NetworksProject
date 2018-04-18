class dataPacket:
    length = 512

    def __init__(self, seqno, data):
        self.seqNo = seqno
        self.data = data



class AckPacket:
    length = 8