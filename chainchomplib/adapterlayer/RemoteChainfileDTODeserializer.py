from chainchomplib.configlayer.ChainfileDeserializer import ChainfileDeserializer

from chainchomplib.exceptions.Exceptions import NotValidException

from chainchomplib.verify.SchemaVerifier import SchemaVerifier

from chainchomplib.data.RemoteChainfileDTO import RemoteChainfileDTO
from chainchomplib.verify.schema.RemoteChainfileDTOSchema import RemoteChainfileDTOSchema


class RemoteChainfileDTODeserializer:

    @staticmethod
    def deserialize(data: dict) -> RemoteChainfileDTO or None:
        try:
            SchemaVerifier.verify(data, RemoteChainfileDTOSchema())
        except NotValidException:
            return None
        else:
            return RemoteChainfileDTO(
                ChainfileDeserializer.deserialize(data['chainfile']),
                data['is_next'],
                data['is_previous'],
                data['remote_link_addr'],
                data['name_of_called_link']
            )
