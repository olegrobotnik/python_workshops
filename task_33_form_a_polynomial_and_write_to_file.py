# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint
from numpy.polynomial import Polynomial
from numpy import polyadd


def poly_coefficients(k):  # Create polynomial coefficients list
    poly_coefficients = [randint(0, 100) for i in range(k)]
    return poly_coefficients


def form_polynomial(poly_coefficients):  # Form polynomials
    poly = Polynomial(poly_coefficients)
    return poly


def print_polynomial(poly):  # Convert polynomial and write-to-file/print
    poly = str(poly)
    poly_list = poly \
        .replace(' ', '') \
        .replace('.0', '') \
        .replace('**', '^') \
        .replace('^1+', '+') \
        .replace('+1x', '+x') \
        .replace('\n', '') \
        .split('+')
    for item in poly_list:
        if item[:2] == '0x':
            poly_list.remove(item)
    # print(f'Converted: \t{poly_list}')
    print(f'Result has been wrote to file: \n{" + ".join(list(reversed(poly_list)))} = 0')
    poly_string = " + ".join(list(reversed(poly_list))) + " = 0"
    with open('task_33_polynomial.txt', 'w') as file:
        file.write(poly_string)


def sum_polynomials(poly1, poly2):
    poly_sum = str(Polynomial(polyadd(poly1, poly2)))
    return poly_sum


k = int(input('Enter the degree of the polynomial: '))
poly1 = form_polynomial(poly_coefficients(k))  # Form polynomial one
poly2 = form_polynomial(poly_coefficients(k))  # Form polynomial two
sum_polynomials = sum_polynomials(poly1, poly2)  # Sum two polynomials
# print_polynomial(poly1)
# print_polynomial(poly2)
print_polynomial(sum_polynomials)
