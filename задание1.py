while True:
    try:
        a = float(input('Введите положительное число a: '))
        if a > 0:
            break
    except:
        print('Неверно. Попробуйте еще раз')

while True:
    try:
        b = float(input('Введите положительное число b, меньшее числа a: '))
        if (a > b) and (b > 0):
            break
    except:
        print('Неверно. Попробуйте еще раз')
while a >= b:
    a = a-b
print('Незанятая часть a:', a)




