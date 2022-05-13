# Вычислить число c заданной точностью d
# Пример: при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)

from math import pi


d = input('Set the accuracy from 0.1 to 0.0000000001: ')
str_pi = str(pi)
num_digits = len(d[2:])
print(pi)
print(float(str_pi[:2 + num_digits]))
