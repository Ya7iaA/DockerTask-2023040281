def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /) or 'q' to quit: ")
            if op.lower() == 'q':
                print("Exiting calculator. Goodbye!")
                break
            b = float(input("Enter second number: "))

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print("Invalid operator! Try again.")
                continue

            print(f"Result: {result}\n")
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")


if __name__ == "__main__":
    calculator()