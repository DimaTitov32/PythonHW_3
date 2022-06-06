# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
numbers = [1.1, 1.2, 3.1, 5, 10.01]
digit = []
for num in numbers:
    frac = round(num % 1, 2)
    if frac > 0:
        digit.append(frac)
print(digit)
print(max(digit) - min(digit))