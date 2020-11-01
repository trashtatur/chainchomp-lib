class ChainlinkConfigModel:

    def __init__(
            self,
            project_name: str,
            chainlink_name: str,
            next_link='',
            previous_link='',
            start='echo "No start script provided"',
            stop='echo "No stop script provided"',
            is_master_link=False,
            mq_type='rabbitmq',
            profile='default'

    ):
        self.is_master_link = is_master_link
        self.stop = stop
        self.start = start
        self.previous_link = previous_link
        self.next_link = next_link
        self.chainlink_name = chainlink_name
        self.project_name = project_name
        self.mq_type = mq_type
        self.profile = profile

    def __eq__(self, other):
        return self.project_name == other.project_name \
            and self.chainlink_name == other.chainlink_name \
            and self.next_link == other.next_link \
            and self.previous_link == other.previous_link \
            and self.start == other.start \
            and self.stop == other.stop \
            and self.is_master_link == other.is_master_link \
            and self.mq_type == other.mq_type \
            and self.profile == other.profile
