# 1st program
# Возведение числа 9 в степень 0.5 и умножение на 5
print(9 ** 0.5 * 5)

# 2nd program
# Проверка логического выражения
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
# Школьная загадка (выражения с и без приоритета)
print(2 * 2 + 2)

print(2 * (2 + 2))

print(2 * 2 + 2 == 2 * (2 + 2))

# 4th program
# Нахождение первой цифры после запятой в числе 123.456
number = '123.456'
float_number = float(number)  # Преобразуем строку в число: 123.456
shifted_number = float_number * 10  # Смещаем первую цифру после точки в целую часть: 1234.56
first_digit_after_point = int(shifted_number) % 10  # Получаем первую цифру после запятой: 4
print(first_digit_after_point)  #or print(int(float('123.456') * 10) % 10)
