from schema import Schema, Or, Optional

from chainchomplib.abstracts.AbstractSchema import AbstractSchema


class ChainlinkSchema(AbstractSchema):
    """
    General schema for chain links. Every one has to adhere to it.
    Sub schemas relate to specific MQ configurations
    """

    def __init__(self):
        super().__init__()

    def init_schema(self) -> Schema:
        return Schema(ChainlinkSchema.get_schema_dict())

    @classmethod
    def get_schema_dict(cls) -> dict:
        return {
            'name': str,
            Optional(Or("next", "previous")): [str],
        }
