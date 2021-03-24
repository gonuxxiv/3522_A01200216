import abc

from Labs.Lab8 import dvd, book
from Labs.Lab8.book import Book
from Labs.Lab8.dvd import DVD
from Labs.Lab8.item import Item
from Labs.Lab8.journal import Journal


class ItemFactory(abc.ABC):
    """
    Abstract ItemFactory class.
    """

    @abc.abstractmethod
    def create_item(self, call_num: str,
                    title: str,
                    num_copies: int,
                    **kwargs) -> Item:
        """
        Creates an Item object.
        :param call_num: a string.
        :param title: a string.
        :param num_copies: an int.
        :param kwargs: keyword args.
        :return: an Item object.
        """
        pass


class BookItemFactory(ItemFactory):
    def create_item(self, call_num: str,
                    title: str,
                    num_copies: int,
                    **kwargs) -> Book:
        return Book(call_num,
                    title,
                    num_copies,
                    kwargs["author"])


class DVDItemFactory(ItemFactory):
    def create_item(self, call_num: str,
                    title: str,
                    num_copies: int,
                    **kwargs) -> DVD:
        return DVD(call_num,
                   title,
                   num_copies,
                   kwargs["release_date"],
                   kwargs["region_code"])


class JournalItemFactory(ItemFactory):
    def create_item(self, call_num: str,
                    title: str,
                    num_copies: int,
                    **kwargs) -> Journal:
        return Journal(call_num,
                       title,
                       num_copies,
                       kwargs["author"],
                       kwargs["issue_number"],
                       kwargs["publisher"])
