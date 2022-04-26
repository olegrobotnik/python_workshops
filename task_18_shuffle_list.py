# Реализовать алгоритм перемешивания списка.

from random import randrange

a = [i for i in range(0, 14)]
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = []
print(a)
n = len(a)
while n > 0:
    j = randrange(n)
    b.append(a[j])
    a.remove(a[j])
    n -= 1
print(b)

# def sattolo_cycle(a) -> None:
#     """Sattolo's algorithm."""
#     i = len(a)
#     while i > 1:
#         i = i - 1
#         j = randrange(i)  # 0 <= j <= i-1
#         a[j], a[i] = a[i], a[j]
#
# sattolo_cycle(a)
# print(a)
