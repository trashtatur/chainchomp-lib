from chainchomplib.verify.SchemaVerifier import SchemaVerifier

from chainchomplib.adapterlayer.Message import Message
from chainchomplib.adapterlayer.MessageHeader import MessageHeader
from chainchomplib.verify.schema.MessageSchema import MessageSchema


class MessageDeserializer:

    @staticmethod
    def deserialize(data: dict) -> Message or None:
        if not SchemaVerifier.verify(data, MessageSchema()):
            return None
        message_header = MessageHeader(
            data['message_header']['origin'],
            data['message_header']['recipients'],
            data['message_header']['adapter_name']
        )
        return Message(
            data['message_body'],
            message_header
        )
