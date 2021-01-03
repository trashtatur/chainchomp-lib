class ChainfileModel:

    def __init__(
            self,
            project_name: str,
            chainlink_name: str,
            next_links=None,
            previous_links=None,
            start='echo "No start script provided"',
            stop='echo "No stop script provided"',
            adapter='rabbitmq',
            profile='default'
    ):
        if next_links is None:
            next_links = []
        if previous_links is None:
            previous_links = []
        self.stop = stop
        self.start = start
        self.previous_links = previous_links
        self.next_links = next_links
        self.chainlink_name = chainlink_name
        self.project_name = project_name
        self.adapter = adapter
        self.profile = profile

    def __eq__(self, other):
        return self.project_name == other.project_name \
            and self.chainlink_name == other.chainlink_name \
            and self.next_links == other.next_links \
            and self.previous_links == other.previous_links \
            and self.start == other.start \
            and self.stop == other.stop \
            and self.adapter == other.adapter \
            and self.profile == other.profile

    def get_serialized(self) -> dict:
        return {
            'project': self.project_name,
            'chainlink': {
                'name': self.chainlink_name,
                'previous': self.previous_links,
                'next': self.next_links
            },
            'start': self.start,
            'stop': self.stop,
            'profile': self.profile,
            'adapter': self.adapter
        }
