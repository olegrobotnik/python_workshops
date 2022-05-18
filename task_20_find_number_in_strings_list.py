# Определить, присутствует ли в заданном списке строк, некоторое число

string_list = ['46765477735435', '123456789',
               'qwerty777фывапрол', 'qwerty778',
               'фывапрол', 'cBd', 'ABC', '7777']
# value = 777
value = int(input('Enter a number to find: '))
count = 0

for item in string_list:
    if str(value) in item:
        count += 1

print(f'Initial list: {string_list}')
print(str(value) + ' is found ' + str(count) + ' time(s).')
