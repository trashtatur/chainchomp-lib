class MessageHeader:

    def __init__(self, origin: str, recipient: str, adapter_name: str):
        self.origin = origin
        self.recipient = recipient
        self.adapter_name = adapter_name

