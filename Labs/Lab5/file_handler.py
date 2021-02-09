import json
from Labs.Lab5.file_extensions import FileExtensions
from Labs.Lab5.invalid_file_type_error import InvalidFileTypeError
from pathlib import Path


class FileHandler:

    @staticmethod
    def load_data(path, file_extension: FileExtensions):
        try:
            if Path(path).exists():
                with open(path, mode='r', encoding='utf-8') as file:
                    if file_extension == FileExtensions.TXT:
                        data = file.read()
                        return data
                    elif file_extension == FileExtensions.JSON:
                        data = json.load(file)
                        print(data)
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
    def write_lines(path, lines):
        try:
            with open(path, mode='a', encoding='utf-8') as file:
                if isinstance(lines, str):
                    file.write(lines + '\n')
                else:
                    raise TypeError("Only str type accepted.")
        except TypeError as e:
            print(f"TypeError caught! Exception: {e}")


file_handler = FileHandler()
file_handler.write_lines("test.txt", "hello")
