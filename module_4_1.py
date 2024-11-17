from fake_math import fake_divide as fake_division
from true_math import true_divide as true_division

# Пример использования
result1 = fake_division(69, 3)
result2 = fake_division(3, 0)
result3 = true_division(49, 7)
result4 = true_division(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)