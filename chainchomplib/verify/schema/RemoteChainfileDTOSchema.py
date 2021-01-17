from schema import Schema

from chainchomplib.abstracts.AbstractSchema import AbstractSchema


class RemoteChainfileDTOSchema(AbstractSchema):

    def init_schema(self) -> Schema:
        return Schema(RemoteChainfileDTOSchema.get_schema_dict())

    @classmethod
    def get_schema_dict(cls) -> dict:
        return {
            'chainfile': dict,
            'is_next': bool,
            'is_previous': bool,
            'remote_link_addr': str,
            'name_of_called_link': str
        }
