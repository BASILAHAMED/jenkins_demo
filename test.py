# main.py

def greet(name):
    """
    A simple function that greets the user.
    """
    return f"Hello, {name}!"

def add_numbers(a, b):
    """
    A function that adds two numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    A function that subtracts two numbers.
    """
    return a - b

# Example usage
name = input("Enter your name: ")
greeting = greet(name)
print(greeting)

result = add_numbers(5, 3)
print("Addition:", result)

result = subtract_numbers(10, 4)
print("Subtraction: ", result)
