import user_interface as ui
import csv


def export_from_file():
    print_type = ui.selection('1 - print to columns', '2 - print to rows')
    if print_type == 1:
        with open('db_row_view.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                print(*row, sep='\n', end='-----\n')
    else:
        with open('db_row_view.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                print(*row, sep=' ', end='\n-----\n')

# export_from_file()
