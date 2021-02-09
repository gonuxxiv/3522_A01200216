from Labs.Lab5.file_handler import FileHandler
from Labs.Lab5.file_extensions import FileExtensions


class Dictionary:
    def __init__(self, filepath):
        self.queried_word = []
        self.dictionary = self.load_dictionary(filepath)

    def load_dictionary(self, filepath):
        return FileHandler.load_data(filepath, FileExtensions.JSON)

    def query_definition(self, word):
        if word in self.dictionary:
            return self.dictionary[word]

    def show_menu(self):
        user_input = None
        while user_input != "exitprogram":
            print("\nEnglish Dictionary")
            print("-----------------------")
            print("Query a word (type 'exitprogram' to quit)")
            user_input = input(">>> ").lower()

            if user_input == '':
                continue

            try:
                definition = self.query_definition(user_input)
                if len(definition) > 0:
                    print(f"{user_input}: {definition}")
                else:
                    print("Could not find the word")
            except:
                pass

        print("\nThanks for using our dictionary!")


def main():
    file = "data.json"
    dictionary = Dictionary(file)
    dictionary.show_menu()


if __name__ == "__main__":
    main()
