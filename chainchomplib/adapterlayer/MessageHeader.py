class MessageHeader:

    def __init__(self, origin: str, recipient: str, mq: str):
        self.origin = origin
        self.recipient = recipient
        self.mq = mq

