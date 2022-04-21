# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = abs(int(input('Enter a number of terms: ')))

sec_list = []
for i in range(N):
    sec_list.append((-3) ** i)
    print(f'\t{sec_list[i]}', end=' ')

# for i in range(0, N + 1):
#     if i < N:
#         print((-3) ** i, end=', ')
#     else:
#         print((-3) ** i, end=', ...')
