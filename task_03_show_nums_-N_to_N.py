# Вывести на экран числа от -N до N

N = abs(int(input('Enter a whole number: ')))
for i in range(-N, N + 1):
    print(i, end=' ')
