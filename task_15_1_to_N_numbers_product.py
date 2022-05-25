# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

from math import factorial

N = int(input('Enter a number of terms: '))
print(*list(map(lambda i: factorial(i), range(1, N + 1))))

# def factorial(N):
#     if N == 0:
#         return 1
#     else:
#         x = N * factorial(N - 1)
#         print(f'{x}', end=' ')
#         return x
#
#
# N = int(input('Enter a number of terms: '))
# factorial(N)


# N = int(input('Enter a number of terms: '))
# factorial(N)
# N= 5
# factorial = 1
# facto = [factorial * i for i in range(1, N+1)]
# print(facto)


# N = int(input('Enter a number of terms: '))
#
# factorial = 1
# for i in range(1, N + 1):
#     factorial = factorial * i
#     if i < N:
#         print(factorial, end=', ')
#     else:
#         print(factorial, end=', ...')
