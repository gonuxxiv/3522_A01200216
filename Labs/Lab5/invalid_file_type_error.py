class InvalidFileTypeError(Exception):
    """
    Error raised when invalid type of the file is given to process.
    """
    def __init__(self, msg):
        super().__init__(msg)
