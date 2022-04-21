# Задать список из n чисел последовательности (1+1/n)**n и вывести
# на экран их сумму

n = int(input('Enter a number: '))
list_n = []
for m in range(1, n + 1):
    list_n.append((1 + 1 / m) ** m)
    print((1 + 1 / m) ** m, end=' ')
print(f'\nSum of numbers in sequence is: {(round(sum(list_n), 2))}')
