# Найти расстояние между двумя точками пространства
import math
import random

# def is_number():
#     while True:
#         try:
#             console_input = int(input("Enter a quadrant: "))
#             return int(console_input)
#         except ValueError:
#             print("It is not a valid number.")


xa = random.randrange(-10, 11)
ya = random.randrange(-10, 11)
za = random.randrange(-10, 11)
xb = random.randrange(-10, 11)
yb = random.randrange(-10, 11)
zb = random.randrange(-10, 11)

distance_between_points = round(math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2), 1)

print(f"Point a: {xa, ya, za} \nPoint b: {xb, yb, zb}")
print(f"The distance between points is {distance_between_points}.")
