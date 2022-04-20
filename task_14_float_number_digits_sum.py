# Подсчитать сумму цифр в вещественном числе.

string_number = str(float(input('Enter a real number: '))).replace('.', '')
list_number = [int(a) for a in string_number]
print(f'Sum of all digits in the real number is {sum(list_number)}.')
