def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    :param a: The first number
    :param b: The second number
    :return: The sum of the two numbers
    """
    return a + b

def subtract_numbers(a, b):
    """
    This function takes two numbers as input and returns their difference.
    
    :param a: The first number
    :param b: The second number
    :return: The difference of the two numbers
    """
    return a - b

# Example usage
if __name__ == "__main__":
    # Get user input for the numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get user input for the operation
    operation = input("Enter the operation (+ for addition, - for subtraction): ")

    if operation == '+':
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    elif operation == '-':
        result = subtract_numbers(num1, num2)
        print(f"The difference between {num1} and {num2} is {result}")
    else:
        print("Invalid operation. Please enter + or -.")
