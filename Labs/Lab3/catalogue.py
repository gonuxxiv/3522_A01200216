import difflib
from Labs.Lab3.book import Book


class Catalogue:

    def __init__(self, book_list):
        """
        Initialize the library with a list of books.
        :param book_list: a sequence of book objects.
        """
        self.book_list = book_list

    def _retrieve_book_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an book with
        the given call number from the library.
        :param call_number: a string
        :return: book object if found, None otherwise
        """
        found_book = None
        for library_book in self.book_list:
            if library_book.call_number == call_number:
                found_book = library_book
                break
        return found_book

    def find_items(self, title):
        """
        Find books with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_book in self.book_list:
            title_list.append(library_book.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new book to the library with a unique call number.
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        book_data = (call_number, title, num_copies)
        author = input("Enter Author Name: ")
        new_book = Book(book_data[0], book_data[1], book_data[2], author)

        found_book = self._retrieve_book_by_call_number(
            new_book.call_number)
        if found_book:
            print(f"Could not add book with call number "
                  f"{new_book.call_number}. It already exists. ")
        else:
            self.book_list.append(new_book)
            print("book added successfully! book details:")
            print(new_book)

    def remove_item(self, call_number):
        """
        Remove an existing book from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_book = self._retrieve_book_by_call_number(call_number)
        if found_book:
            self.book_list.remove(found_book)
            print(f"Successfully removed {found_book.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"book with call number: {call_number} not found.")
