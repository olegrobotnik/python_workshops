# 41.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:
# 12W1B12W3B24W1B14W

# message = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
message = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'


def rle(message):
    encoded_string = ''
    count = 1
    char = message[0]
    for i in range(1, len(message)):
        if message[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = message[i]
            count = 1
    encoded_string = encoded_string + str(count) + char
    return encoded_string


print(message)
print(rle(message))
