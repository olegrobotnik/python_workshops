# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле positions.txt в одной строке одно число

N = 7
sequence = []

for j in range(-N, N + 1):
    sequence.append(j)
print('\n\tIndex:')
for y in range(0, len(sequence)):
    print(f"\t{y}", end=' ')
print('\n\tSequence:')
for i in sequence:
    print(f"\t{i}", end=' ')


print()
# print(sequence)

# N = abs(int(input('Enter a number: ')))


file = open('positions.txt', 'w')

positions = [1, 2, 3, 4, 5]
for i in positions:
    file.write('%d \n' % i)
file.close()

pos_list = []
file = open('positions.txt', 'r')
content = file.readlines()
for line in content:
    pos_list.append(int(line))

# print(pos_list)
# print(line)
