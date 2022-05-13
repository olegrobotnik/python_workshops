# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

# N = int(input('Enter a number of terms: '))
#
# factorial = 1
# for i in range(1, N + 1):
#     factorial = factorial * i
#     if i < N:
#         print(factorial, end=', ')
#     else:
#         print(factorial, end=', ...')

N = int(input('Enter a number of terms: '))

def factorial(N):
    if N == 0:
        return 1
    else:
        x = N * factorial(N - 1)
        print(f'{x}', end=' ')
        return x

factorial(N)
