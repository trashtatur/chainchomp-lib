from schema import Schema, Optional

from chainchomplib.abstracts.AbstractSchema import AbstractSchema
from chainchomplib.verify.schema.ChainlinkSchema import ChainlinkSchema


class ChainfileSchema(AbstractSchema):

    def __init__(self):
        super().__init__()

    def init_schema(self) -> Schema:
        return Schema(ChainfileSchema.get_schema_dict())

    @classmethod
    def get_schema_dict(cls):
        return {
            'project': str,
            'chainlink': ChainlinkSchema.get_schema_dict(),
            Optional('start'): str,
            Optional('stop'): str,
            Optional('profile'): str,
            Optional('adapter'): str
        }
