# Указав номер четверти прямоугольной системы координат, показать
# допустимые значения координат для точек этой четверти

def is_number():
    while True:
        try:
            console_input = int(input("Enter a quadrant: "))
            return int(console_input)
        except ValueError:
            print("It is not a valid number.")


quadrant = is_number()

if 1 <= quadrant <= 4:
    if quadrant == 1:
        print("x-axis: from 0 to ∞ \ny-axis: from 0 to ∞")
    elif quadrant == 2:
        print("x-axis: from ∞, 0 \ny-axis: from 0 to ∞")
    elif quadrant == 3:
        print("x-axis: from ∞ to 0 \ny-axis: from ∞ to 0")
    elif quadrant == 4:
        print("x-axis: from 0 to ∞ \ny-axis: from ∞ to 0")
else:
    print("It is not a quadrant.")
