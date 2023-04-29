def say_hello():
    print('Hello, World <3')

# say_hello()

'''
Оголоси функцію з назвою print_sum. Тіло функції має містити змінні a = 7 та b = 9, вивід їх суми.
Виклич функцію.
'''

def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*' + ' '*8 + '*')
    print('*' * 10)


# for i in range(10):
#     draw_box()

def draw_triangle(x):
    for i in range(x):
        i += 1
        print('*' * i)

# draw_triangle()

# size_of_triangle = int(input())

# draw_triangle(size_of_triangle)

def print_max(a, b):
    if a > b:
        print(f'Max - {a}')
    elif a == b:
        print('They are equal')
    else:
        print(f'Max - {b}')


x = 15
y = 7

# print_max(x, y)

'''
Напиши функцію, яка приймає на вхід прізвище студента, і виводить персональне привітання.
--> Hello Ivan
'''

# def plus(a, b):
#     result = a + b
#     return result


# # res = plus(3, 4)
# # print(plus(3, 4))
# plus(3, 4)

def suma(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def power(a, b):
    return a ** b

def multiply(a, b):
    return a * b


def calculation(operand_A, operand_B, operator):
    if operator not in ['+', '-', '*', '^']:
        print('Invalid operator')
    else:
        match operator:
            case '+':
                result = suma(operand_A, operand_B)
            case '-':
                result = subtraction(operand_A, operand_B)
            case '*':
                result = multiply(operand_A, operand_B)
            case '^':
                result = power(operand_A, operand_B)

        print(operand_A, operator, operand_B, '=', result)


a = float(input('Enter the first operand: '))
b = float(input('Enter the second operand: '))

print('Available operators - [+, -, *, ^]')

operation = input('Enter the operation: ')

calculation(operand_A=a, operand_B=b, operator=operation)