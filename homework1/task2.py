# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# for X in 0, 1:
# for Y in 0, 1:
# for Z in 0, 1:
# rint(X, Y, Z)
# print('Истина' if not (X or Y or Z) == (not X and not Y and not Z) else 'Ложь')

res = (not (x or y or z) == (not x and not y and not z) for x in range(2) for y in range(2) for z in range(2)) # здесь res это генератор
print(all(res))


