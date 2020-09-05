class Message:

    def __init__(self, message_body='', message_header=None):
        self._message_body = message_body
        self.message_header = message_header
