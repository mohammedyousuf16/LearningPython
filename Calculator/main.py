try:
    a = int(input('enter the first number: '))
    b = int(input('enter the second number: '))

    print("Enter the operation you want to perform.\npress + for addition\npress - for subtraction\npress * for multiplication\npress / for divition")

    operation= input("Enter the operation you want to perform")
    match operation:
        case '+':
            print(f'the result is {a + b}')
        case '-':
            print(f'the result is {a - b}')
        case '*':
            print(f'the result is {a * b}')
        case '/':
            print(f'the result is {a / b}')

except Exception as e:
    print('enter a valid value for a & b')