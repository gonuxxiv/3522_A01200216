from Labs.Lab8.item import Item


class Journal(Item):
    """
    Represents a single journal in a library which is identified through
    it's call number.
    """
    def __init__(self, call_num, title, num_copies, author, issue_number, publisher):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :param issue_number: an int
        :param publisher: a string
        """
        super().__init__(call_num, title, num_copies)
        self._author = author
        self._issue_number = issue_number
        self._publisher = publisher

    def __str__(self):
        """
        Print the object.
        :return: a description of the instance in a formatted string
        """
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"
