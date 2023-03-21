#calculator.py

# Create a basic calculator that calculates different functions

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    return a / b

def exp(a,b):
    return a ** b


while(True):
    print('Pick a function to perform:')
    print('  1) Add')
    print('  2) Subtract')
    print('  3) Multiply')
    print('  4) Divide')
    print('  5) Exponent')
    print('  6) Quit')

    choice = int(input('Please enter choice(1-6): '))

    if choice == 1:
        a = int(input('Please pick the first number to add: '))
        b = int(input('Please pick the second number to add: '))
        print(f'The sum of {a} and {b} is {add(a,b)}')

    elif choice == 2:
        a = int(input('Please pick the first number to subtract: '))
        b = int(input('Please pick the second number to subtract: '))
        print(f'The difference of {a} and {b} is {subtract(a,b)}')

    elif choice == 3:
        a = int(input('Please pick the first number to multiply: '))
        b = int(input('Please pick the second number to multiply: '))
        print(f'The product of {a} and {b} is {multiply(a,b)}')

    elif choice == 4:
        a = int(input('Please pick the first number to divide: '))
        b = int(input('Please pick the second number to divide: '))
        print(f'The division of {a} and {b} is {divide(a,b)}')

    elif choice == 5:
        a = int(input('Please pick the first number for the base of the exponent: '))
        b = int(input('Please pick the second number to increase the base by that power: '))
        print(f'{a} to the power of {b} is {exp(a,b)}')
        
    else:
        print('Thank you for using my calculator')
        break