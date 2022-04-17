# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат

def tru_statement(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")


tru_statement(0, 0, 0)
tru_statement(0, 0, 1)
tru_statement(0, 1, 0)
tru_statement(0, 1, 1)
tru_statement(1, 0, 0)
tru_statement(1, 0, 1)
tru_statement(1, 1, 0)
tru_statement(1, 1, 1)
