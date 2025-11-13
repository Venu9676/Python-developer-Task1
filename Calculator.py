# calculator.py
# A simple CLI Calculator App

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("Welcome to the CLI Calculator!")
    print("Available operations: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Enter operation (+, -, *, /, exit): ")

        if choice == "exit":
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "+":
            print("Result:", add(num1, num2))
        elif choice == "-":
            print("Result:", subtract(num1, num2))
        elif choice == "*":
            print("Result:", multiply(num1, num2))
        elif choice == "/":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please select +, -, *, /, or exit.")

if __name__ == "__main__":
    calculator()
