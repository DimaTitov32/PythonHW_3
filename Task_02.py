# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for i, num in enumerate(numbers):
    if i == len(numbers)//2:
        if len(numbers) % i == 0:
            exit()
        else:
            print(f"Результат = {numbers[i] * numbers[-i - 1]}")
            exit()
    else:
        print(f"Результат = {numbers[i] * numbers[-i - 1]}")
