# Подсчитать сумму цифр в вещественном числе.

n = float(input('Enter a real number: '))
str_n = str(n).replace('.', '')
list_n = [int(item) for item in str_n]
dig_sum = 0
for item in list_n:
    dig_sum += item

print(f'Sum of all digits in the real number is {dig_sum}.')

# string_number = str(float(input('Enter a real number: '))).replace('.', '')
# list_number = [int(a) for a in string_number]
# print(f'Sum of all digits in the real number is {sum(list_number)}.')
