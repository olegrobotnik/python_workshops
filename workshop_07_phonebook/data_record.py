# import user_interface as ui


def make_a_record():
    name = input("Enter a name: ")
    surname = input("Enter a surname: ")
    phone_number = input("Enter a phone number: ")
    description = input("Enter a description: ")
    with open('db_column_view.csv', 'a') as file:
        file.write(f'{name}\n{surname}\n{phone_number}\n{description}\n\n')
    with open('db_row_view.csv', 'a') as file:
        file.write(f'{name};{surname};{phone_number};{description};\n')
    print('Entry recorded.')

# make_a_record()
