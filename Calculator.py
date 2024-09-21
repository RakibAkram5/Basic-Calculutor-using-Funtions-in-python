def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by 0"
    return a / b

def exponent(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by 0"
    return a % b

def getNumber(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculator():
    """Main function to run the Calculator"""
    print("Welcome to the Calculator")
    while True:
        print("\nPlease select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Modulus (%)")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = getNumber("Enter the first number: ")
            num2 = getNumber("Enter the second number: ")

            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'
            elif choice == '5':
                result = exponent(num1, num2)
                operation = '^'
            elif choice == '6':
                result = modulus(num1, num2)
                operation = '%'

            print(f"\nResult: {num1} {operation} {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
