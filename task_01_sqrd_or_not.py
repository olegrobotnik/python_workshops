# По двум заданным числам проверить является ли одно квадратом второго

# a=3
# b=9

a, b = map(int, input('Enter whole numbers space separated: ').split())
print(bool(a == b ** 2 or b == a ** 2))
