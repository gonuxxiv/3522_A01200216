import des
import ast
import argparse
import abc
import enum


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """
    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:
    """
    Crypto class.
    """
    def __init__(self):
        """
        Initialize Crypto class.
        """
        print("\n\n--------- Setting up handlers ----------\n")
        encryption_handler = EncryptionHandler()
        decryption_handler = DecryptionHandler()
        encryption_validate_key = ValidateKeyHandler()
        encryption_validate_data = ValidateDataHandler()
        encryption_output = ValidateOutputHandler()
        decryption_validate_key = ValidateKeyHandler()
        decryption_validate_data = ValidateDataHandler()
        decryption_output = ValidateOutputHandler()

        # set up order
        encryption_validate_key.set_handler(encryption_validate_data)
        encryption_validate_data.set_handler(encryption_output)
        encryption_output.set_handler(encryption_handler)

        decryption_validate_key.set_handler(decryption_validate_data)
        decryption_validate_data.set_handler(decryption_output)
        decryption_output.set_handler(decryption_handler)

        self.encryption_start_handler = encryption_validate_key
        self.decryption_start_handler = decryption_validate_key

    def execute_request(self, request: Request):
        """
        Set up appropriate handler to execute request.
        :param request: Request object
        """
        if request.encryption_state == CryptoMode.EN:
            self.encryption_start_handler.execute_request(request)
        elif request.encryption_state == CryptoMode.DE:
            self.decryption_start_handler.execute_request(request)


class BaseCryptoHandler(abc.ABC):
    """
    BaseCryptoHandler class, a base class for handling encryption/decryption.
    """
    def __init__(self, next_handler=None):
        """
        Initialize BaseCryptoHandler class.
        :param next_handler: next handler
        """
        self.next_handler = next_handler

    @abc.abstractmethod
    def execute_request(self, request: Request) -> bool:
        """
        Execute requested data.
        :param request: Request object
        """
        pass

    def set_handler(self, handler):
        """
        Set new handler.
        :param handler: next handler class
        """
        self.next_handler = handler


class ValidateKeyHandler(BaseCryptoHandler):
    """
    ValidateKeyHandler class.
    """
    def execute_request(self, request: Request) -> bool:
        """
        Validates key for the data.
        :param request: Request object
        :return: True if it's the end of the chain, False if something went wrong
        """
        print("Handler is validating key")
        if request.key is not None:
            if not self.next_handler:
                return True
            return self.next_handler.execute_request(request)
        else:
            print("Key is not valid")
            return False


class ValidateDataHandler(BaseCryptoHandler):
    """
    ValidateDataHandler class.
    """
    def execute_request(self, request: Request):
        """
        Validates Data of the data.
        :param request: Request object
        :return: True if it's the end of the chain, False if something went wrong
        """
        print("Handler is validating data")
        if request.data_input is not None or request.input_file is not None:
            if not self.next_handler:
                return True
            return self.next_handler.execute_request(request)
        else:
            print("Data is not validated")
            return False


class ValidateOutputHandler(BaseCryptoHandler):
    """
    ValidateOutputHandler class.
    """
    def execute_request(self, request: Request):
        """
        Validates output for the data.
        :param request: Request object
        :return: True if it's the end of the chain, False if something went wrong
        """
        print("Handler is validating output")
        if request.output is not None:
            if not self.next_handler:
                return True
            return self.next_handler.execute_request(request)
        else:
            print("Output is not validated")
            return False


class EncryptionHandler(BaseCryptoHandler):
    """
    EncryptionHandler class.
    """
    def execute_request(self, request: Request):
        """
        Execute requested data for an encryption.
        :param request: Request object
        """
        print("Handler is executing encryption")
        byte_key = bytes(request.key, encoding='utf-8')  # get key handler
        key = des.DesKey(byte_key)
        encrypted_data = None

        if request.data_input is not None:  # read data handler
            byte_data = bytes(request.data_input, encoding='utf-8')
            encrypted_data = key.encrypt(byte_data, padding=True)
        elif request.input_file is not None:
            with open(request.input_file, mode='rb') as file:
                lines = file.read()
            encrypted_data = key.encrypt(lines, padding=True)

        if request.output != "print":  # output handler
            with open(request.output, mode='wb+') as file:
                file.write(encrypted_data)
            print("\nEncrypted data is saved in a file.")
        else:
            print("\nEncrypted Data:")
            print(encrypted_data)

        return True


class DecryptionHandler(BaseCryptoHandler):
    """
    DecryptionHandler class.
    """
    def execute_request(self, request: Request):
        """
        Execute requested data for a decryption.
        :param request: Request object
        """
        print("Handler is executing decryption")
        byte_key = bytes(request.key, encoding='utf-8')
        key = des.DesKey(byte_key)
        decrypted_data = None

        if request.data_input is not None:
            data = ast.literal_eval(request.data_input)
            decrypted_data = key.decrypt(data, padding=True)
        elif request.input_file is not None:
            with open(request.input_file, mode='rb') as file:
                lines = file.readline()
            data = ast.literal_eval(str(lines))
            decrypted_data = key.decrypt(data, padding=True)

        if request.output != "print":
            with open(request.output, mode='w+') as file:
                data = str(decrypted_data)[2:-1]
                file.write(data)
            print("\nDecrypted data is saved in a file.")
        else:
            print("\nDecrypted Data:")
            print(str(decrypted_data)[2:-1])

        return True


def main(request: Request):
    crypto = Crypto()
    crypto.execute_request(request)


if __name__ == '__main__':
    req = setup_request_commandline()
    main(req)
