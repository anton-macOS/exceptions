# # Реалізуйте функцію, яка ділить два числа, але обробляє
# # помилку ZeroDivisionError, якщо друге число дорівнює нулю.
# first_num = int(input('Введіть перше число: '))
# second_num = int(input('Введіть друге число: '))
#
# try:
#     result = first_num / second_num
#     print(result)
# except ZeroDivisionError:
#     print('Не можна ділити на гуль')


# Напишіть програму, яка відкриває файл для читання та обробляє
# помилку FileNotFoundError, якщо файл не знайдено.
# try:
#     file = open('file.txt', 'r')
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print('Файл не знайдено')


# # Створіть програму, яка отримує від користувача два інпути,
# # конвертує цей інпут до числа і відловлює помилку, якщо конвертувати не вийшло.
# first_num = input('1) Введіть: ')
# second_num = input('2) Введіть: ')
#
#
# def convertation(number):
#     try:
#         number = float(number)
#         return f'Число {number} конвертовано'
#     except ValueError:
#         return 'Інпут не є числом'
#
#
# print(convertation(first_num))
# print(convertation(second_num))


# Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст,
# виводячи рядки, які є у першому файлі, але відсутні у другому.
# first_file = open('file.txt', 'r')
# second_file = open('example.txt', 'r')
#
# first_line = set(first_file.readlines())
# second_line = set(second_file.readlines())
# diff = first_line.difference(second_line)
# print('Рядки які є в першому файлі, але нема в другому:')
# for line in diff:
#     print(line)
#
# first_file.close()
# second_file.close()


# Реалізуйте програму, яка копіює вміст одного файлу в інший.

#
# def copy_to_file(first_file, second_file):
#     first_open = open(first_file, 'r')
#     second_open = open(second_file, 'w')
#     copy_file = first_open.read()
#     second_open.write(copy_file)
#     first_open.close()
#     second_open.close()
#
#
# copy_to_file('file.txt', 'example.txt')


# Створіть функцію, яка приймає рядок від користувача та записує його у файл.

# def save_to_file(file_name):
#     text = input('Enter text: ')
#     file = open(file_name, 'w+')
#     file.write(text)
#     file.close()
#
#
# save_to_file('file.txt')


# Обробіть виняток IndexError, коли програма намагається отримати
# ʼдоступ до неправильного індексу в списку.
# fruit_list = ['apple', 'orange', 'grape']
#
# try:
#     print(fruit_list[3])
# except IndexError:
#     print('Такого індексу не існує')


# Напишіть програму, яка пропонує користувачу ввести список чисел,
# відокремлених комами. Перетворіть введений рядок у список цілих чисел
# і обробляйте помилки ValueError (у випадку невірного введення цілих чисел)
# та IndexError (у випадку доступу до індексів, що виходять за межі діапазону).
# try:
#     numbers = input('Enter numbers: ')
#     number_list = [int(num) for num in numbers.split(',')]
#     print(number_list)
# except ValueError:
#     print('Введено не ціле число')
# except IndexError:
#     print('Нема такого індекса')


# Напишіть програму, яка читає вміст текстового файлу
# та виводить кількість слів у ньому.
# def count_words(file_name):
#     file = open(file_name, 'r')
#     print(len(file.read().split()))
#
#
# count_words('file.txt')
