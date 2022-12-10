# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = int(input("Введите число для точности числа Пи: "))
print(f'Число Пи с заданной точностью {d} равно {round(pi, d)}')


# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def prime_factor(n):
    i = 2
    num = []
    while i * i <= n:
        while n % i == 0:
            num.append(i)
            n //= i
        i = i + 1
    if n > 1:
        num.append(n)
    return num


print(prime_factor(int(input('Введите число для разложения на простые множители: '))))

# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {lst}")
mod_lst = []
[mod_lst.append(i) for i in lst if i not in mod_lst]
print(f"Список без повторяющихся элементов: {mod_lst}")

# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def write_file(st):
    with open('file.txt', 'w') as data:
        data.write(st)
    data.close()


k = int(input('Введите натуральную степень k: '))
ratio = [randint(0, 100) for i in range(k)] + [randint(1, 100)]
part = '+'.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(ratio) if j][::-1])

part = part.replace('x^1+', 'x+').replace('x^0', '')
poly = part.replace('x^0', '')
part += ('', '1')[poly[-1] == '+']
if k != 0:
    part = "{0} = 0".format(part)
# print(f'\nУравнение многочлена: {part} при натуральной степени {k}')
str_pos = str(part)
write_file(str_pos)
