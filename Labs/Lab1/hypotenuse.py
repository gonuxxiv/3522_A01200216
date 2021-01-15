import math


def calculate_hypotenuse(a: int, b: int) -> float:
    """Calculate hypotenuse.

    The function calculates hypotenuse of a right-angled triangle.

    :param a: a positive number
    :param b: a positive number
    :return: a value of the hypotenuse
    """
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    return hypotenuse


def sum(a: int, b: int) -> int:
    """Do summation.

    The function performs summation using two given values.

    :param a: a positive number
    :param b: a positive number
    :return: the result of the summation
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """Do multiplication.

    The function performs multiplication using two given values.

    :param a: a positive number
    :param b: a positive number
    :return: the result of the multiplication
    """
    return a * b


def divide(a: int, b: int) -> float:
    """Do division.

    The function performs division using two given values.

    :param a: a positive number
    :param b: a positive number
    :return: the result of the division
    """
    return a / b


def subtract(a: int, b: int) -> int:
    """Do subtraction.

    The function performs subtraction using two given values.

    :param a: a positive number
    :param b: a positive number
    :return: the result of the subtraction
    """
    return a - b


if __name__ == "__main__":
    print("1 to calculate hypotenuse\n"
          "2 to add\n"
          "3 to subtract\n"
          "4 to multiply\n"
          "5 to divide")
    user_input = int(input(">>> "))

    if user_input >= 6:
        print("Wrong input, try again")
    else:
        a = int(input("Length of a: "))
        b = int(input("Length of b: "))
        if user_input == 1:
            hypotenuse = calculate_hypotenuse(a, b)
            print(f"Hypotenuse = {hypotenuse}")
        elif user_input == 2:
            result = sum(a, b)
            print(f"The sum = {result}")
        elif user_input == 3:
            result = subtract(a, b)
            print(f"The subtraction = {result}")
        elif user_input == 4:
            result = multiply(a, b)
            print(f"The multiplication = {result}")
        elif user_input == 5:
            result = divide(a, b)
            print(f"The division = {result}")
