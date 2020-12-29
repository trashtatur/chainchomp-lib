from schema import Schema

from chainchomplib.abstracts.AbstractSchema import AbstractSchema


class ProjectFileSchema(AbstractSchema):

    def init_schema(self) -> Schema:
        return Schema(ProjectFileSchema.get_schema_dict())

    @classmethod
    def get_schema_dict(cls) -> dict:
        return {
            'name': str,
            'chainlinks': [str]
        }
