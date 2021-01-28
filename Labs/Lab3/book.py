from Labs.Lab3.item import Item


class Book(Item):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """
    def __init__(self, call_num, title, num_copies, author):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._author = author

    def __str__(self):
        """
        Print the object.
        :return: a description of the instance in a formatted string
        """
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}"
