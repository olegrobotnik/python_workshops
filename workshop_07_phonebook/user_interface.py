from texttable import Texttable


def welcome_screen():
    table = Texttable()
    table.header(["Greetings! The phonebook welcomes you."])
    table.add_row(["Select an option: "])
    table.add_row([f"1 - to make a record\n2 - to export a record"])
    table.set_cols_align(['l'])
    print(table.draw())
    choice = int(input("Selection: "))
    return choice


def selection(option_1, option_2):
    table = Texttable()
    table.add_row(["Select an option: "])
    # table.add_row([f"1 - record to columns\n2 - record to rows"])
    table.add_row([option_1 + '\n' + option_2])
    table.set_cols_align(['l'])
    print(table.draw())
    user_selection = int(input("Selection: "))
    return user_selection
