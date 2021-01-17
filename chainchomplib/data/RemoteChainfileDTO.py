from chainchomplib.configlayer.model.ChainfileModel import ChainfileModel


class RemoteChainfileDTO:

    def __init__(
            self,
            chainfile_model: ChainfileModel,
            is_next: bool,
            is_previous: bool,
            remote_link_addr: str
    ):
        self.chainfile_model = chainfile_model
        self.is_next = is_next
        self.is_previous = is_previous
        self.remote_link_addr = remote_link_addr

    def get_serialized(self) -> dict:
        return {
            'chainfile': self.chainfile_model.get_serialized(),
            'is_next': self.is_next,
            'is_previous': self.is_previous,
            'remote_link_addr': self.remote_link_addr
        }
