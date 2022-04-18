# Сообщить в какой четверти координатной плоскости или на какой оси
# находится точка с координатами Х и У

def is_number():
    while True:
        try:
            a, b = map(float, input("Enter coordinates x, y space separated: ").split())
            # x = float(input("Enter coordinate x: "))
            # y = float(input("Enter coordinate y: "))
            return float(a), float(b)
        except ValueError:
            print("Are not valid coordinates.")


x, y = is_number()

if x == 0 and y == 0:
    print("The point is at the origin.")
elif (x > 0 or x < 0) and y == 0:
    print("The point is on the x-axis.")
elif x == 0 and (y > 0 or y < 0):
    print("The point is on the y-axis.")
elif x > 0 < y:
    print('The point is in I quadrant.')
elif x < 0 < y:
    print('The point is in II quadrant.')
elif x < 0 > y:
    print('The point is in III quadrant.')
elif x > 0 > y:
    print('The point is in IV quadrant.')
