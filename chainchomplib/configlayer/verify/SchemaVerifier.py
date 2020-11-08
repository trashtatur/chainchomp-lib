from schema import Schema, SchemaError

from chainchomplib.configlayer.verify import SchemaBuilder
from chainchomplib.exceptions.Exceptions import ChainfileNotValidException


class SchemaVerifier:

    @classmethod
    def verify(cls, data: dict, schema: Schema) -> bool:
        try:
            built_schema = SchemaBuilder.build_schema_from_dict(data)
            return schema.validate(built_schema)
        except SchemaError as error:
            raise ChainfileNotValidException(
                f'Provided chainfile config file data was not valid with exception: {error.autos} ',
                error
            )
