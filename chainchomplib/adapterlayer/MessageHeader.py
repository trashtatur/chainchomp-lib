from typing import List


class MessageHeader:

    def __init__(self, origin: str, recipients: List[str], adapter_name: str):
        self.origin = origin
        self.recipients = recipients
        self.adapter_name = adapter_name

