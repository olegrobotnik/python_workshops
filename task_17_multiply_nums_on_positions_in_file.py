# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле positions.txt в одной строке одно число

# N = int(input('Enter a number: '))

file = open('positions.txt', 'w')

data = [1, 2, 3, 4, 5]
for i in data:
    file.write('%d \n' % i)
file.close()

pos_list = []
file = open('positions.txt', 'r')
content = file.readlines()
for line in content:
    pos_list.append(int(line))

print(pos_list)
# print(line)
