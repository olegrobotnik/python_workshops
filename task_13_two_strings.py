# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# str1= input('First string: ')
# str2= input('Second string: ')

str1 = 'Python free 777 $$$ python free python python python $$$ python'
str2 = 'python free new $$$'

str_list = str1.lower().split()
substr_list = str2.lower().split()

print('String: ' + str1)
print('Substrings: ' + str2)
print()

for i in substr_list:
    count = 0
    for j in str_list:
        count = str_list.count(i)
    print(f'{i} found {count} times.')


# # Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
#
# # str1= input('First string: ')
# # str2= input('Second string: ')
#
# str1 = 'Python free 777 $$$ python free python python python $$$ python'
# str2 = 'python free new $$$'
#
# str_list = str1.lower().split()
# substr_list = str2.lower().split()
#
# counter = {}
# for substr_element in substr_list:
#     substr = substr_element
#     for str_element in str_list:
#         if str_element == substr:
#             counter[str_element] = counter.get(str_element, 0) + 1
#
# same_words = {element: count for element, count in counter.items() if count > 0}
#
# print('String: ' + str1)
# print('Substrings: ' + str2)
# print()
# print(same_words)
