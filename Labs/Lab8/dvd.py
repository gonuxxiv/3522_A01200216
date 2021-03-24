from Labs.Lab3.item import Item


class DVD(Item):
    """
    Represents a single DVD in a library which is identified through
    it's call number.
    """
    def __init__(self, call_num, title, num_copies, release_date, region_code):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param release_date: a string
        :param region_code: an int
        """
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        """
        Print the object.
        :return: a description of the instance in a formatted string
        """
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}"
