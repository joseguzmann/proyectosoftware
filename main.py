import os


def sum_function(a: float, b: float) -> float:
    pass


def subtract_function(a: float, b: float) -> float:
    pass


def multiply_function(a: float, b: float) -> float:
    return a*b


def menu():
    prompt = f"""
    Very simple calculator.
    1. Sum two numbers
    2. subtract two numbers
    3. Multiply two numbers
    Choose one:
    """
    print(prompt)


def main():
    while True:
        menu()
        selection = int(input())
        os.system('cls' if os.name == 'nt' else 'clear')

        if (selection == 1):
            a = input("First number:")
            b = input("Second number:")
            print(sum_function(float(a), float(b)))
        elif (selection == 2):
            a = input("First number:")
            b = input("Second number:")
            print(subtract_function(a, b))
        elif (selection == 3):
            a = input("First number:")
            b = input("Second number:")
            print(multiply_function(float(a), float(b)))


if __name__ == "__main__":
    main()
