# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле positions.txt в одной строке одно число


N = abs(int(input('Enter a number from 1 to 9: ')))
# N = 7
sequence = []

for j in range(-N, N + 1):
    sequence.append(j)
print('\n\tPosition:')
for y in range(1, len(sequence) + 1):
    print(f"\t{y}", end=' ')
print('\n\tSequence:')
for i in sequence:
    print(f"\t{i}", end=' ')

file = open('positions.txt', 'w')

positions = [3, 13, 15]
for i in positions:
    file.write('%d \n' % i)
file.close()

pos_list = []
file = open('positions.txt', 'r')
content = file.readlines()
for line in content:
    pos_list.append(int(line))

print('\n\tMultiplied positions from .txt file: ')
for k in pos_list:
    print(f"\t{k}", end=' ')

selected_list = [sequence[i - 1] for i in pos_list]
print(f"\n\t{selected_list}")
result = 1
for m in selected_list:
    result = result * m
print('\tProduct of numbers: ')
print(f"\t{result}")
