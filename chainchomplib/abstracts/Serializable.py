import abc


class Serializable(abc.ABC):

    @abc.abstractmethod
    def get_serialized(self) -> dict:
        pass
