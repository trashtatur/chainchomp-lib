from schema import Schema


class SchemaVerifier:

    @classmethod
    def verify(cls, data: dict, schema: Schema) -> bool:
        return schema.validate(data)
