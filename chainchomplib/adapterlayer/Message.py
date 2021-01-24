from chainchomplib.abstracts.Serializable import Serializable
from chainchomplib.adapterlayer.MessageHeader import MessageHeader


class Message(Serializable):

    def __init__(self, message_body, message_header: MessageHeader):
        self.message_body = message_body
        self.message_header = message_header

    def get_serialized(self) -> dict:
        return {
            'message_body': self.message_body,
            'message_header': {
                'origin': self.message_header.origin,
                'recipients': self.message_header.recipients,
                'adapter_name': self.message_header.adapter_name,
            }
        }

