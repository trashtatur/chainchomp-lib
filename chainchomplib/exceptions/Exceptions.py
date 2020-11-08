class ChainfileNotValidException(Exception):
    """
    This exception gets thrown when a
    chainfile is not valid
    """
    def __init__(self, previous, message):
        self.previous = previous
        self.message = message
