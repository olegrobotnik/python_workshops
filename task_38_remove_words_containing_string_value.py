# 38.	Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'
# Выходные данные: 'лповап ываываыв'

string = 'ываабв лповап абвцукв алоабвабв ываываыв'
value = 'абв'
string_list = string.split(' ')
list = []
cut_string = ''

for substring in string_list:
    if substring.find('абв') == -1:
        list.append(substring)

    # if value not in substring:
    #     cut_string += substring + ' '

cut_string = ' '.join(list)

print(string)
print(cut_string)
