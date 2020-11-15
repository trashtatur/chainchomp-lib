from schema import SchemaError

from chainchomplib.abstracts.AbstractConfigSchema import AbstractConfigSchema
from chainchomplib.configlayer.verify import SchemaBuilder
from chainchomplib.exceptions.Exceptions import NotValidException


class SchemaVerifier:

    @staticmethod
    def verify(data: dict, schema: AbstractConfigSchema) -> bool:
        try:
            built_schema = SchemaBuilder.build_schema(schema)
            return built_schema.validate(data)
        except SchemaError as error:
            raise NotValidException(
                f'Provided data was not valid with exception: {error.autos} ',
                error
            )
