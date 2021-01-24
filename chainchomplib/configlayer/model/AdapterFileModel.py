from chainchomplib.abstracts.Serializable import Serializable


class AdapterFileModel(Serializable):
    def __init__(
            self,
            name: str,
            path: str,
            start: str,
            stop: str
    ):
        self.name = name
        self.path = path
        self.start = start
        self.stop = stop

    def __eq__(self, other):
        return self.name == other.name \
               and self.path == other.path \
               and self.start == other.start \
               and self.stop == other.stop

    def get_serialized(self) -> dict:
        return {
            'name': self.name,
            'path': self.path,
            'start': self.start,
            'stop': self.stop
        }