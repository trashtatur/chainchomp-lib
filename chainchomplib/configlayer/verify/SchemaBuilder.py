from schema import Schema

from chainchomplib.abstracts.AbstractConfigSchema import AbstractConfigSchema


def build_schema(schema_data: AbstractConfigSchema) -> Schema:
    return Schema(schema_data.get_schema_dict())

