from chainchomplib.abstracts.Serializable import Serializable
from chainchomplib.configlayer.model.ChainfileModel import ChainfileModel


class RemoteChainfileDTO(Serializable):

    def __init__(
            self,
            chainfile_model: ChainfileModel,
            is_next: bool,
            is_previous: bool,
            remote_link_addr: str,
            name_of_called_link: str
    ):
        self.chainfile_model = chainfile_model
        self.is_next = is_next
        self.is_previous = is_previous
        self.remote_link_addr = remote_link_addr
        self.name_of_called_link = name_of_called_link

    def get_serialized(self) -> dict:
        return {
            'chainfile': self.chainfile_model.get_serialized(),
            'is_next': self.is_next,
            'is_previous': self.is_previous,
            'remote_link_addr': self.remote_link_addr,
            'name_of_called_link': self.name_of_called_link
        }
