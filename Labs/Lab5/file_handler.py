import json
from Labs.Lab5.file_extensions import FileExtensions
from Labs.Lab5.invalid_file_type_error import InvalidFileTypeError
from pathlib import Path


class FileHandler:
    """
    Process file loading and file writing.
    """
    @staticmethod
    def load_data(path: str, file_extension: FileExtensions):
        """Load a file.

        The function loads a file of two different extensions: .txt and .json.

        :param path: string
        :param file_extension: FileExtensions enum object
        :return: dictionary if the file is json, string if the file is in txt
        """
        try:
            if Path(path).exists():
                with open(path, mode='r', encoding='utf-8') as file:
                    if file_extension == FileExtensions.TXT:
                        data = file.read()
                        return data
                    elif file_extension == FileExtensions.JSON:
                        data = json.load(file)
                        return data
                    else:
                        raise InvalidFileTypeError("Invalid file extension detected!")
            else:
                raise FileNotFoundError("File name doesn't exist.")
        except FileNotFoundError as e:
            print(f"FileNotFoundError caught! Exception: {e}")
        except InvalidFileTypeError as e:
            print(f"InvalidFileTypeError caught! Exception: {e}")

    @staticmethod
    def write_lines(path: str, lines: str):
        """Write text on the file.

        The function writes a text on the file in the given path. If the
        file doesn't exist, it creates a new one.

        :param path: string
        :param lines: string
        """
        try:
            with open(path, mode='a', encoding='utf-8') as file:
                if isinstance(lines, str):
                    file.write(lines + '\n')
                else:
                    raise TypeError("Only str type accepted.")
        except TypeError as e:
            print(f"TypeError caught! Exception: {e}")
