# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

from random import randint

# Enter the sequence of numbers and the empty resulting list
sequence = []
result = []
for i in range(100):
    sequence.append(randint(0, 50))

# If the value is unique, put it in the resulting list
# for i in sequence:
#     if i not in result:
#         result.append(i)

# Or create a set and convert it to the list
result = list(set(sequence))

# Print results
print('Original sequence: \t' + str(sorted(sequence)))
print(f'Unique sequence: \t{sorted(result)}')
print(f'Original sequence length: \t{len(sequence)}')
print(f'Unique sequence length: \t{len(result)}')
