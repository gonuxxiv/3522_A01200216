import difflib

from Labs.Lab5.file_handler import FileHandler
from Labs.Lab5.file_extensions import FileExtensions


class Dictionary:
    """
     Represents an English Dictionary; user can query a word and get its
     definitions.
     """
    def __init__(self):
        """Create a new instance of Dictionary object.

        The function initializes new Dictionary object.

        :precondition: "data.json" file in the same directory
        :postcondition: Assigns data in "data.json" file to itself as a dictionary
        """
        self.dictionary = self.load_dictionary("data.json")

    def load_dictionary(self, filepath: str):
        """Load a file.

        The function loads a file using method in the FileHandler class.

        :param filepath: string
        :return: dictionary of a dictionary
        """
        return FileHandler.load_data(filepath, FileExtensions.JSON)

    def query_definition(self, word: str):
        """Find a word.

        The function searches if the queried word exists and return the definition of the word.

        :param word: string
        :return: definition as a list if found, otherwise just an empty character
        """
        if word in self.dictionary:
            FileHandler.write_lines("queried_words.txt", word)
            return self.dictionary[word]
        else:
            return ''

    def show_menu(self):
        """Show dictionary menu.

        The function prompts a user to query a word and find its definition.
        """
        user_input = None
        while user_input != "exitprogram":
            print("\nEnglish Dictionary")
            print("-----------------------")
            print("Query a word (type 'exitprogram' to quit)")
            user_input = input(">>> ").lower()

            if user_input == '':
                continue

            definition = self.query_definition(user_input)
            if len(definition) > 0:
                print(f"{user_input}: {definition}")
            else:
                possible_result = difflib.get_close_matches(user_input, self.dictionary.keys(),
                                                            cutoff=0.85)
                if len(possible_result) > 0:
                    print("\nCould not find the word, but here are some possible results:")
                    print(possible_result)
                else:
                    if user_input != "exitprogram":
                        print("Could not find the word")

        print("\nThanks for using our dictionary!")


def main():
    dictionary = Dictionary()
    dictionary.show_menu()


if __name__ == "__main__":
    main()
