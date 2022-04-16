# Вывести на экран числа от -N до N

N = abs(int(input('Enter a number: ')))
for i in range(-N, N + 1):
    print(i, end=' ')
