from schema import Schema

from chainchomplib.abstracts.AbstractSchema import AbstractSchema


def build_schema(schema_data: AbstractSchema) -> Schema:
    return Schema(schema_data.get_schema_dict())

