"""
This module is responsible for holding a BookAnalyzer class that is optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":","(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        # strip out empty lines and convert list of lines to list of words
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text += line.split()
        self.text = stripped_text

        # count each word in the list to the dictionary
        temp_text = {}
        for word in self.text:
            temp_word = word
            if temp_word in temp_text:
                temp_text[temp_word] += 1
            else:
                temp_text[temp_word] = 1
        self.text = temp_text

        # remove common punctuation and append the word to new dict
        temp_dict_words = {}
        for word in self.text:
            temp_word = word
            for punctuation in self.COMMON_PUNCTUATION:
                temp_word = temp_word.replace(punctuation, '')
            temp_dict_words[temp_word] = self.text[word]
        self.text = temp_dict_words

    # @staticmethod
    # def is_unique(word, word_list):
    #     """
    #     Checks to see if the given word appears in the provided sequence.
    #     This check is case in-sensitive.
    #     :param word: a string
    #     :param word_list: a sequence of words
    #     :return: True if not found, false otherwise
    #     """
    #     if word in word_list:
    #         return False
    #     return True

    def find_unique_words(self):
        """
        Filters out all the words in the text.
        :return: a list of all the unique words.
        """
        temp_text = self.text

        unique_words = []
        for x, y in temp_text.items():
            if y == 1:
                unique_words.append(x)
        return unique_words


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-"*50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-"*50)
    for word in unique_words:
        print(word)
    print("-"*50)


if __name__ == '__main__':
    main()
