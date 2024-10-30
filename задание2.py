import math
while True:
    try:
        x = float(input('Введите действительное число x: '))
        break
    except:
        print('Неверно >:(. Попробуйте еще раз')

while True:
    try:
        n = int(input('Введите натуральное число n: '))
        break
    except:
        print('Неверно >:(. Попробуйте еще раз')
r = 0
for i in range(1, n+1):
    r += (x**i)/math.factorial(i)
print('Результат -', r)
