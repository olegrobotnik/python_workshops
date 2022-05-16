# 31.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Enter a natural number: '))
primes = []

if N > 1:
    for i in range(2, N + 1):
        while N % i == 0:
            primes.append(i)
            N = N / i
    print('Prime numbers: ')
    print(*primes, sep = ', ')
    # print(', '.join(str(x) for x in primes))
else:
    print('This is one.')
