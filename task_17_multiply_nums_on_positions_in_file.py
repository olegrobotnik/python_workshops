# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле task_17_positions.txt в одной строке одно число

import numpy as np

N = abs(int(input('Enter a number from 1 to 9: ')))

sequence = [i for i in range(-N, N + 1)]
file = open('task_17_positions.txt', 'r')
positions_list = [int(line) for line in file.readlines()]
print(*sequence)
print(*positions_list)
product = np.prod([sequence[i] for i in positions_list])
print(product)

# import numpy as np
#
# N = abs(int(input('\tEnter a number from 1 to 9: ')))

# sequence = []
#
# for j in range(-N, N + 1):
#     sequence.append(j)
# print('\n\tPosition:')
# for y in range(1, len(sequence) + 1):
#     print(f"\t{y}", end=' ')
# print('\n\tSequence:')
# for i in sequence:
#     print(f"\t{i}", end=' ')
#
# file = open('task_17_positions.txt', 'w')
#
# positions = list(map(int, input('\n\tSelect positions to multiply: ').split()))
#
# for i in positions:
#     file.write('%d \n' % i)
# file.close()
#
# pos_list = []
# file = open('task_17_positions.txt', 'r')
# content = file.readlines()
# for line in content:
#     pos_list.append(int(line))
#
# print('\n\tMultiplied positions from .txt file: ')
# for k in pos_list:
#     print(f"\t{k}", end=' ')
#
# print()
# selected_list = [sequence[i - 1] for i in pos_list]
# for p in selected_list:
#     print(f"\t{p}", end=' ')
#
# print(f"\n\t{selected_list}")
# print(f"\n\tProduct of numbers: {np.prod(selected_list)}")  # Цикл умножения элементов списка с помощью библиотеки numpy
