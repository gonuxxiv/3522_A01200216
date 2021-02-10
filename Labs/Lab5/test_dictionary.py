import io
from unittest import TestCase
from Labs.Lab5.dictionary import Dictionary
from unittest.mock import patch


class TestDictionary(TestCase):

    dictionary = Dictionary()

    def test_query_definition_find_word(self):
        word = "rain"
        expected = ['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.',
                    'To fall from the clouds in drops of water.']
        actual = self.dictionary.query_definition(word)
        self.assertEqual(expected, actual)

    def test_query_definition_word_not_found(self):
        word = "ajvlkajvad"
        expected = ''
        actual = self.dictionary.query_definition(word)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['', 'exitprogram'])
    def test_show_menu_empty_query(self, inp, mock_stdout):
        self.dictionary.show_menu()
        expected = "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "\nThanks for using our dictionary!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['afadf', 'exitprogram'])
    def test_show_menu_word_not_found(self, inp, mock_stdout):
        self.dictionary.show_menu()
        expected = "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "Could not find the word\n" \
                   "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "\nThanks for using our dictionary!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['RAInn', 'exitprogram'])
    def test_show_menu_show_possible_result(self, inp, mock_stdout):
        self.dictionary.show_menu()
        expected = "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "\nCould not find the word, but here are some possible results:\n" \
                   "['rain']\n" \
                   "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "\nThanks for using our dictionary!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['rain', 'exitprogram'])
    def test_show_menu_word_found(self, inp, mock_stdout):
        self.dictionary.show_menu()
        expected = "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "rain: ['Precipitation in the form of liquid water drops with diameters " \
                   "greater than 0.5 millimetres.', 'To fall from the clouds in drops of water.']\n" \
                   "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "\nThanks for using our dictionary!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['exitprogram'])
    def test_show_menu_exit_program(self, inp, mock_stdout):
        self.dictionary.show_menu()
        expected = "\nEnglish Dictionary\n" \
                   "-----------------------\n" \
                   "Query a word (type 'exitprogram' to quit)\n" \
                   "\nThanks for using our dictionary!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
