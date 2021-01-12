import math


def CalculateHypotenuse(a, b):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    return hypotenuse


def Sum(a, b):
    return a + b


def Multiply(a, b):
    return a * b


def Divide(a, b):
    return a / b


def Subtract(a, b):
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
            hypotenuse = CalculateHypotenuse(a, b)
            print(f"Hypotenuse = {hypotenuse}")
        elif user_input == 2:
            result = Sum(a, b)
            print(f"The sum = {result}")
        elif user_input == 3:
            result = Subtract(a, b)
            print(f"The subtraction = {result}")
        elif user_input == 4:
            result = Multiply(a, b)
            print(f"The multiplication = {result}")
        elif user_input == 5:
            result = Divide(a, b)
            print(f"The division = {result}")
