from schema import SchemaError

from chainchomplib.abstracts import AbstractSchema
from chainchomplib.exceptions.Exceptions import NotValidException


class SchemaVerifier:

    @staticmethod
    def verify(data: dict, schema: AbstractSchema) -> bool:
        try:
            built_schema = schema.init_schema()
            return built_schema.validate(data)
        except SchemaError as error:
            raise NotValidException(
                f'Provided data was not valid with exception: {error.autos} ',
                error
            )
