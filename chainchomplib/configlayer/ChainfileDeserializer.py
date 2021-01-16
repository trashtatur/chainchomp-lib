from chainchomplib.exceptions.Exceptions import NotValidException

from chainchomplib.configlayer.model.ChainfileModel import ChainfileModel

from chainchomplib.verify.schema.ChainfileSchema import ChainfileSchema

from chainchomplib.verify.SchemaVerifier import SchemaVerifier


class ChainfileDeserializer:

    @staticmethod
    def deserialize(data: dict) -> ChainfileModel or None:
        try:
            SchemaVerifier.verify(data, ChainfileSchema())
        except NotValidException:
            return None
        else:
            return ChainfileModel(
                data['project'],
                data['chainlink']['name'],
                data['chainlink']['next'],
                data['chainlink']['previous'],
                data['start'],
                data['stop'],
                data['adapter'],
                data['profile']
            )
