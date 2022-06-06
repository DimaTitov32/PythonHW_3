# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = 22
digit = ''
while number > 0:
    digit = f"{number % 2}" + digit
    number //= 2
print(digit)