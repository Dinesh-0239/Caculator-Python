from art import logo
from clear_screen import clear_screen

def add(num1,num2):
    return num1 + num2
    
def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def calculation():    
    print(logo)
    choice = True
    result = int(input("What's the first number?: "))
    while choice:
        operation_list = {
                    '+' : add, 
                    '-' : subtract,
                    '*' : multiply,
                    '/' : divide
                    }
        operation = input("+\n-\n*\n/\nPick an operation: ")
        if operation not in list(operation_list.keys()):
            print("Invalid Input!")
        else:
            num = int(input("What's the next number?: "))
            operation_method = operation_list[operation]
            print(f"{result} {operation} {num} = {operation_method(result,num)}")
            result = operation_method(result, num)
            if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower() != 'y':
                choice = False
                if input(f"Type 'y' to continue using calculator or type 'n' to exit: ").lower() != 'y':
                    exit()
            clear_screen()
            print(logo)
    clear_screen()
    calculation()
        

    
calculation()