from Labs.Lab3.book import Book
from Labs.Lab3.dvd import DVD
from Labs.Lab3.journal import Journal


class LibraryItemGenerator:

    @staticmethod
    def add_item():
        user_input = None
        while user_input != 4:
            print("\nWhat is the item type to add?")
            print("-----------------------")
            print("1. Book")
            print("2. DVD")
            print("3. Journal")
            print("4. Quit")
            string_input = input("Please enter your choice (1-4)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                book = LibraryItemGenerator.add_book()
                return book
            elif user_input == 2:
                dvd = LibraryItemGenerator.add_DVD()
                return dvd
            elif user_input == 3:
                journal = LibraryItemGenerator.add_journal()
                return journal
                return journal
            elif user_input == 4:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")

    @staticmethod
    def add_book():
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
        return new_book

    @staticmethod
    def add_DVD():
        """
        Add a brand new book to the library with a unique call number.
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        release_date = input("Enter a release date: ")
        region_code = input("Enter a region code: ")
        dvd_data = (call_number, title, num_copies, release_date, region_code)
        new_dvd = DVD(dvd_data[0], dvd_data[1], dvd_data[2], dvd_data[3], dvd_data[4])
        return new_dvd

    @staticmethod
    def add_journal():
        """
        Add a brand new book to the library with a unique call number.
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        author = input("Enter Author Name: ")
        issue_number = int(input("Enter a issue number: "))
        publisher = input("Enter a publisher: ")
        journal_data = (call_number, title, num_copies, author, issue_number, publisher)

        new_journal = Journal(journal_data[0], journal_data[1], journal_data[2], journal_data[3],
                              journal_data[4], journal_data[5])
        return new_journal
