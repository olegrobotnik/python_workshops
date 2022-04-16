# Дано число обозначающее день недели. Вывести его название и указать является
# ли он выходным.

# weekday_number = int(input("Enter a weekday number: "))

def try_parse_int():
    while True:
        try:
            console_input = int(input("Enter a weekday number: "))
            return int(console_input)
        except ValueError:
            print("Is not a valid number.")


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
weekday_number = try_parse_int()

if 1 <= weekday_number <= 7:
    if weekday_number == 6 or weekday_number == 7:
        print(f"{weekdays[weekday_number - 1]} is a weekend.")
    else:
        print(f"{weekdays[weekday_number - 1]} is a business day.")
else:
    print("Is not a valid number.")
    weekday_number = try_parse_int()
