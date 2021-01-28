""" This module houses the library"""
from Labs.Lab3.book import Book
from Labs.Lab3.catalogue import Catalogue
from Labs.Lab3.dvd import DVD
from Labs.Lab3.journal import Journal


class Library:
    """
    The Library consists of a list of books, dvds, and journals and provides an
    interface for users to check out, return and find items.
    """
    def __init__(self, catalogue):
        self.catalogue = catalogue

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of items, check out, return, find, add, remove an item.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            #handle user pressing only enter in menu
            if(string_input == ''):
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.catalogue.display_available_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self.catalogue.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self.catalogue.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                self.catalogue.find_items(input_title)

            elif user_input == 5:
                self.catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item")
                self.catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")


def generate_test_items():
    """
    Return a list of items with dummy data.
    :return: a list
    """
    item_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss"),
        Journal("432.12.432", "Can Apes Speak?", 2, "Dr. Johnson", 5, "Penguin"),
        DVD("777.77.777", "The Avengers", 3, "2012/04/11", 1)
    ]
    return item_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    item_list = generate_test_items()
    catalogue = Catalogue(item_list)
    my_epic_library = Library(catalogue)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
