from chainchomplib.abstracts.AbstractDeserializer import AbstractDeserializer
from chainchomplib.exceptions.Exceptions import NotValidException

from chainchomplib.verify.SchemaVerifier import SchemaVerifier

from chainchomplib.adapterlayer.Message import Message
from chainchomplib.adapterlayer.MessageHeader import MessageHeader
from chainchomplib.verify.schema.MessageSchema import MessageSchema


class MessageDeserializer(AbstractDeserializer):

    @staticmethod
    def deserialize(data: dict) -> Message or None:
        try:
            SchemaVerifier.verify(data, MessageSchema())
        except NotValidException:
            return None
        else:
            message_header = MessageHeader(
                data['message_header']['origin'],
                data['message_header']['recipients'],
                data['message_header']['adapter_name']
            )
            return Message(
                data['message_body'],
                message_header
            )
