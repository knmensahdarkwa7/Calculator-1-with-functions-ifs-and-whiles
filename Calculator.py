print("Welcome to my calculator")

# Function definitions
def add():
    num1 = int(input('Pls enter the first number: '))
    num2 = int(input('Pls enter the second number: '))
    return num1 + num2

def sub():
    num1 = int(input('Pls enter the first number: '))
    num2 = int(input('Pls enter the second number: '))
    return num1 - num2

def expo():
    num1 = int(input('Pls enter the first number: '))
    num2 = int(input('Pls enter the second number: '))
    return num1 * num2

def div():
    num1 = int(input('Pls enter the first number: '))
    num2 = int(input('Pls enter the second number: '))
    if num2 == 0:
        return "Error: Division by zero is not allowed!"
    return num1 / num2

# Operator selection
operator = input('Which operator (+, -, *, /): ')

# Dictionary mapping operators to functions
operations = {
    '+': add,
    '-': sub,
    '*': expo,  
    '/': div
}

# Execute the selected operation
if operator in operations:
    print(operations[operator]())  # Calls the function from the dictionary
else:
    print("Invalid operator! Please use +, -, *, or /.")