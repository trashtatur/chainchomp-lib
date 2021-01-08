from chainchomplib.configlayer.model.ChainfileModel import ChainfileModel

from chainchomplib.verify.schema.ChainfileSchema import ChainfileSchema

from chainchomplib.verify.SchemaVerifier import SchemaVerifier


class ChainfileDeserializer:

    @staticmethod
    def deserialize(data: dict) -> ChainfileModel or None:
        if not SchemaVerifier.verify(data, ChainfileSchema()):
            return None
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
