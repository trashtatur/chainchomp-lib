from schema import SchemaError

from chainchomplib.abstracts.AbstractSchema import AbstractSchema
from chainchomplib.verify import SchemaBuilder
from chainchomplib.exceptions.Exceptions import NotValidException


class SchemaVerifier:

    @staticmethod
    def verify(data: dict, schema: AbstractSchema) -> bool:
        try:
            built_schema = SchemaBuilder.build_schema(schema)
            return built_schema.validate(data)
        except SchemaError as error:
            raise NotValidException(
                f'Provided data was not valid with exception: {error.autos} ',
                error
            )
