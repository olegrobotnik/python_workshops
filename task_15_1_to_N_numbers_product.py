# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

N = int(input('Enter a number of terms: '))

factorial = 1
for i in range(1, N + 1):
    factorial = factorial * i
    if i < N:
        print(factorial, end=', ')
    else:
        print(factorial, end=', ...')
