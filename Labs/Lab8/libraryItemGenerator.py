from Labs.Lab8.book import Book
from Labs.Lab8.dvd import DVD
from Labs.Lab8.item_factory import ItemFactory, BookItemFactory, DVDItemFactory, JournalItemFactory
from Labs.Lab8.journal import Journal


class LibraryItemGenerator:
    """
    Provide user with a list of library item types and do specific operation for specific object.
    """

    @staticmethod
    def add_item():
        """
        Prompts user for the type of the item to instantiate and return it.
        :return: an object
        """
        user_input = None
        while user_input != 4:
            print("\nWhat is the item type to add?")
            print("-----------------------")
            print("1. Book")
            print("2. DVD")
            print("3. Journal")
            print("4. Quit")
            string_input = input("Please enter your choice (1-4) ")

            if string_input == '':
                continue

            user_input = int(string_input)

            call_number = input("\nEnter Call Number: ")
            title = input("Enter title: ")
            num_copies = int(input("Enter number of copies "
                                   "(positive number): "))

            if user_input == 1:
                author = input("Enter Author Name: ")
                book = BookItemFactory().create_item(call_number,
                                                     title,
                                                     num_copies,
                                                     author=author)
                return book
            elif user_input == 2:
                release_date = input("Enter a release date: ")
                region_code = input("Enter a region code: ")
                dvd = DVDItemFactory().create_item(call_number,
                                                   title,
                                                   num_copies,
                                                   release_date=release_date,
                                                   region_code=region_code)
                return dvd
            elif user_input == 3:
                author = input("Enter Author Name: ")
                issue_number = int(input("Enter a issue number: "))
                publisher = input("Enter a publisher: ")
                journal = JournalItemFactory().create_item(call_number,
                                                           title,
                                                           num_copies,
                                                           author=author,
                                                           issue_number=issue_number,
                                                           publisher=publisher)
                return journal
            elif user_input == 4:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")
