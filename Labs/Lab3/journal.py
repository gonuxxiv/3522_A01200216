from Labs.Lab3.item import Item


class Journal(Item):
    def __init__(self, call_num, title, num_copies, author, issue_number, publisher):
        super().__init__(call_num, title, num_copies)
        self._author = author
        self._issue_number = issue_number
        self._publisher = publisher

    def __str__(self):
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"
