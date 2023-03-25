'''
📎 ДЗ:
У окремому модулі оголосити функцію Sign(X) цілого типу, що повертає для дійсного числа X наступні
значення : 
−1, якщо X < 0;
0, якщо X = 0;
1, якщо X > 0.
У файлі main.py за допомогою цієї функції знайти значення виразу Sign(A) + Sign(B) для даних дійсних
чисел A та B.
'''

def Sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print('Sign.py module started')
    print(Sign(-4))