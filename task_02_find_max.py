# Найти максимальное из пяти чисел

# print(max(1, 7, 99, 77, 333,))

a, b, c, d, e = 3, 5, 2, 333, 1
max_number = a
if max_number < b:
    max_number = b
if max_number < c:
    max_number = c
if max_number < d:
    max_number = d
if max_number < e:
    max_number = e
print(max_number)
