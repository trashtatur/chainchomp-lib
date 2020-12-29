from schema import Schema

from chainchomplib.abstracts.AbstractSchema import AbstractSchema


class RegisteredChainlinkSchema(AbstractSchema):

    def init_schema(self) -> Schema:
        return Schema(RegisteredChainlinkSchema.get_schema_dict())

    @classmethod
    def get_schema_dict(cls) -> dict:
        return {
            'name': str,
            'path': str,
        }
