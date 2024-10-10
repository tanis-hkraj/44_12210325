import math

# Basic Arithmetic Operations
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
       return "Error: Cannot divide by zero."

# Additional Operations
def modulus(a, b):
    return a % b

def percentage(a, b):
    return (a / 100) * b

def quotient(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: Cannot divide by zero."

def square(a):
    return a ** 2

def square_root(a):
    return math.sqrt(a)

def cube(a):
    return a ** 3

# Area calculations
def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return math.pi * radius ** 2

# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Percentage")
print("7. Quotient")
print("8. Square")
print("9. Square Root")
print("10. Cube")
print("11. Area of Rectangle")
print("12. Area of Circle")

while True:
    # Take input from the user
    choice = input("\nEnter choice(1-12): ")

    # Check if the user selects a valid operation
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

        elif choice in ('8', '9', '10'):
            try:
                num1 = float(input("Enter the number: "))
            except ValueError:
                print("Invalid input. Please enter a number only.")
                continue

        elif choice == '11':
            try:
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

        elif choice == '12':
            try:
                radius = float(input("Enter the radius of the circle: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

        # Perform the chosen operation
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))

        elif choice == '6':
            print(num1, "% of", num2, "=", percentage(num1, num2))

        elif choice == '7':
            print("Quotient of", num1, "and", num2, "=", quotient(num1, num2))

        elif choice == '8':
            print(num1, "squared =", square(num1))

        elif choice == '9':
            print("Square root of", num1, "=", square_root(num1))

        elif choice == '10':
            print("Cube of", num1, "=", cube(num1))

        elif choice == '11':
            print("Area of the rectangle =", area_rectangle(length, width))

        elif choice == '12':
            print("Area of the circle =", area_circle(radius))

        # Ask the user if they want to continue
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid input. Please enter a valid choice (1-12).")

print("Thank you for using the calculator!")
