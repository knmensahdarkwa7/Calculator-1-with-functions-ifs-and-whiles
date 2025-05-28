print("Welcome to my calculator")

operator = input('Which operator (q to quit): ')

while  not operator == "q" :
    if operator == '+':
        def add():
            num1 = int(input('Pls enter the first number: '))
            num2 = int(input('Pls enter the second number: '))
            return num1 + num2

        print(add())
        operator = input('Which operator (q to quit): ')# Call the function using parentheses

    if operator == '-':
        def sub():
            num1 = int(input('Pls enter the first number: '))
            num2 = int(input('Pls enter the second number: '))
            return num1 - num2

        print(sub())
        operator = input('Which operator (q to quit): ')# Call the function using parentheses

    if operator == 'x':
        def expo():
            num1 = int(input('Pls enter the first number: '))
            num2 = int(input('Pls enter the second number: '))
            return num1 * num2

        print(expo())
        operator = input('Which operator (q to quit): ')# Call the function using parentheses

    if operator == '/':
        def div():
            num1 = int(input('Pls enter the first number: '))
            num2 = int(input('Pls enter the second number: '))
            return num1 / num2

        print(div())
        operator = input('Which operator (q to quit): ')# Call the function using parentheses