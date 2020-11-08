from schema import Schema, SchemaError

from chainchomplib.abstracts.AbstractConfigSchema import AbstractConfigSchema
from chainchomplib.configlayer.verify import SchemaBuilder
from chainchomplib.exceptions.Exceptions import ChainfileNotValidException


class SchemaVerifier:

    @classmethod
    def verify(cls, data: dict, schema: AbstractConfigSchema) -> bool:
        try:
            built_schema = SchemaBuilder.build_schema(schema)
            return built_schema.validate(data)
        except SchemaError as error:
            raise ChainfileNotValidException(
                f'Provided chainfile config file data was not valid with exception: {error.autos} ',
                error
            )
