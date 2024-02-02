import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number"

def power(x, y):
    return x ** y

def sine(angle_in_degrees):
    return math.sin(math.radians(angle_in_degrees))

def cosine(angle_in_degrees):
    return math.cos(math.radians(angle_in_degrees))

def tangent(angle_in_degrees):
    return math.tan(math.radians(angle_in_degrees))

def calculator():
    print("Advanced Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")

    choice = input("Enter operation number (1-9): ")

    if choice in ['1', '2', '3', '4', '6']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(x, y)}")
        elif choice == '2':
            print(f"Result: {subtract(x, y)}")
        elif choice == '3':
            print(f"Result: {multiply(x, y)}")
        elif choice == '4':
            print(f"Result: {divide(x, y)}")
        elif choice == '6':
            print(f"Result: {power(x, y)}")

    elif choice in ['5']:
        x = float(input("Enter a number: "))
        print(f"Result: {square_root(x)}")

    elif choice in ['7', '8', '9']:
        angle = float(input("Enter the angle in degrees: "))
        if choice == '7':
            print(f"Result: {sine(angle)}")
        elif choice == '8':
            print(f"Result: {cosine(angle)}")
        elif choice == '9':
            print(f"Result: {tangent(angle)}")

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    calculator()
