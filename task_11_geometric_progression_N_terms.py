# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = abs(int(input('Enter a number of terms: ')))

for i in range(0, N + 1):
    if i < N:
        print((-3) ** i, end=', ')
    else:
        print((-3) ** i, end=', ...')
