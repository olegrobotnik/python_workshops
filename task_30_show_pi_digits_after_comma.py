# Вычислить число c заданной точностью d
# Пример: при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)

from math import pi


def try_parse_int():
    while True:
        try:
            console_input = int(input('Set the accuracy from 1 to 10 digits after the decimal point: '))
            if 1 <= console_input <= 10:
                return console_input
            else:
                print("It is not a valid number.")
        except ValueError:
            print("It is not a valid number.")


d = try_parse_int()
str_pi = str(pi)
print(f"The number pi with a given accuracy {10 ** (-d):.10f} is {str_pi[:2 + d]}.")

# d = input('Set the accuracy from 0.1 to 0.0000000001: ')
# str_pi = str(pi)
# num_digits = len(d[2:])
# print(pi)
# print(float(str_pi[:2 + num_digits]))
