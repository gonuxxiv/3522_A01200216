import difflib
from Labs.Lab3.libraryItemGenerator import LibraryItemGenerator


class Catalogue:
    """
    Catalogue holds list of items and perform the library operations.
    """
    def __init__(self, item_list):
        """
        Initialize the catalogue of items.
        :param item_list: a sequence of item objects.
        """
        self._item_list = item_list

    def check_out(self, call_number):
        """
        Check out an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_book = self._retrieve_item_by_call_number(call_number)
        if library_book.check_availability():
            status = self.reduce_item_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find item with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_item_count(call_number)
        if status:
            print("item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def _retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.
        :param call_number: a string
        :return: book object if found, None otherwise
        """
        found_item = None
        for library_item in self._item_list:
            if library_item.call_number == call_number:
                found_item = library_item
                break
        return found_item

    def find_items(self, title):
        """
        Find items with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_item in self._item_list:
            if title == library_item.get_title():
                print("Found an item!")
                print(library_item)
                return
            else:
                title_list.append(library_item.get_title())

        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)

        if len(results) > 0:
            print("We found the following:")
            for title in results:
                print(title)
        else:
            print("Sorry! We found nothing with that title")

    def add_item(self):
        """
        Add a brand new item to the library with a unique call number.
        """
        new_item = LibraryItemGenerator.add_item()

        found_item = self._retrieve_item_by_call_number(
            new_item.call_number)
        if found_item:
            print(f"Could not add item with call number "
                  f"{new_item.call_number}. It already exists. ")
        else:
            self._item_list.append(new_item)
            print("item added successfully! item details:")
            print(new_item)

    def remove_item(self, call_number):
        """
        Remove an existing item from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_item = self._retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("Items List")
        print("--------------", end="\n\n")
        for library_item in self._item_list:
            print(library_item)

    def reduce_item_count(self, call_number):
        """
        Decrement the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count decremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_number):
        """
        Increment the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count incremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False
