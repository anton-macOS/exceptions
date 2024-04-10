# Реалізуйте функцію, яка ділить два числа, але обробляє
# помилку ZeroDivisionError, якщо друге число дорівнює нулю.
first_num = int(input('Введіть перше число: '))
second_num = int(input('Введіть друге число: '))

try:
    result = first_num / second_num
    print(result)
except ZeroDivisionError:
    print('Не можна ділити на гуль')
