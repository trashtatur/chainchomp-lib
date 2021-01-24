import abc


class AbstractDeserializer(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def deserialize(data: dict):
        pass