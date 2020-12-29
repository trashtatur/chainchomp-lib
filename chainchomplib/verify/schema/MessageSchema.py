from chainchomplib.abstracts.AbstractSchema import AbstractSchema
from schema import Schema


class MessageSchema(AbstractSchema):

    def init_schema(self) -> Schema:
        return Schema(MessageSchema.get_schema_dict())

    @classmethod
    def get_schema_dict(cls) -> dict:
        return {
            'message_body': str,
            'message_header': {
                'origin': str,
                'recipients': [str],
                'adapter_name': str
            }
        }
