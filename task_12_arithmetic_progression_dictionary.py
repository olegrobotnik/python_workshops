# Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print({n: 3 * n + 1 for n in range(1, abs(int(input('Enter a number of terms: '))))})

# dictionary = {}
#
# for i in range(1, N + 1):
#     dictionary[i] = 3 * i + 1
#
# print(dictionary)
