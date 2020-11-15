class ChainfileModel:

    def __init__(
            self,
            project_name: str,
            chainlink_name: str,
            next_link='',
            previous_link='',
            start='echo "No start script provided"',
            stop='echo "No stop script provided"',
            adapter='rabbitmq',
            profile='default'
    ):
        self.stop = stop
        self.start = start
        self.previous_link = previous_link
        self.next_link = next_link
        self.chainlink_name = chainlink_name
        self.project_name = project_name
        self.adapter = adapter
        self.profile = profile

    def __eq__(self, other):
        return self.project_name == other.project_name \
            and self.chainlink_name == other.chainlink_name \
            and self.next_link == other.next_link \
            and self.previous_link == other.previous_link \
            and self.start == other.start \
            and self.stop == other.stop \
            and self.adapter == other.adapter \
            and self.profile == other.profile
