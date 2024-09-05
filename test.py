def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    :param a: The first number
    :param b: The second number
    :return: The sum of the two numbers
    """
    return a + b

#Subtraction function
def subtract_numbers(a, b):
    """
    This function takes two numbers as input and returns their difference.
    
    :param a: The first number
    :param b: The second number
    :return: The difference of the two numbers
    """
    return a - b

#Multiplication function
def multiply_numbers(a, b):
    """
    This function takes two numbers as input and returns their product.
    
    :param a: The first number
    :param b: The second number
    :return: The product of the two numbers
    """
    return a * b

#Division function
def divide_numbers(a, b):
    """
    This function takes two numbers as input and returns their quotient.
    
    :param a: The first number
    :param b: The second number
    :return: The quotient of the two numbers
    :raises ValueError: If the second number (divisor) is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Example usage
if __name__ == "__main__":
    # Get user input for the numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get user input for the operation
    operation = input("Enter the operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

    if operation == '+':
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    elif operation == '-':
        result = subtract_numbers(num1, num2)
        print(f"The difference between {num1} and {num2} is {result}")
    elif operation == '*':
        result = multiply_numbers(num1, num2)
        print(f"The product of {num1} and {num2} is {result}")
    elif operation == '/':
        try:
            result = divide_numbers(num1, num2)
            print(f"The quotient of {num1} and {num2} is {result}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation. Please enter +, -, *, or /.")
        