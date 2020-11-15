from chainchomplib.adapterlayer.MessageHeader import MessageHeader


class Message:

    def __init__(self, message_body, message_header: MessageHeader):
        self._message_body = message_body
        self.message_header = message_header
