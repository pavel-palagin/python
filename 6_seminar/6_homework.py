# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# data = input('enter the expression: ')
# data = '12+5*(15-6/3)'
#
# operators = {
#     '(': 0,
#     ')': 0,
#     '+': 1,
#     '-': 1,
#     '*': 2,
#     '/': 2,
# }




# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах
# (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).

# def rle_pres(data):
#     code = ''
#     char = ''
#     count = 1
#     for i in data:
#         if i != char:
#             if char:
#                 code += str(count) + char
#             count = 1
#             char = i
#         else:
#             count += 1
#     else:
#         code += str(count) + char
#     return code
#
# pac_data = rle_pres('AAAAAAABBBBCCDDDDFFFEEEY')
# print(pac_data)
#
# def rle_unpack(data):
#     decode = ''
#     count = ''
#     for char in data:
#         if char.isdigit():
#              count += char
#         else:
#              decode += char * int(count)
#              count = ''
#     return decode
# unpac_data = rle_unpack(pac_data)
# print(unpac_data)



# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13. Если в строку включены числа или специальные символы, они должны быть возвращены как есть.
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode
#
# text = 'Big city light!!!'
#
# def rot13(text):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     code = ''
#     for i in text:
#         if i in alphabet:
#             if alphabet.index(i) < 13:
#                 code += alphabet[alphabet.index(i) + 13]
#             else:
#                 code += alphabet[alphabet.index(i) - 13]
#         elif i in alphabet.upper():
#             if alphabet.upper().index(i) < 13:
#                 code += alphabet.upper()[alphabet.upper().index(i) + 13]
#             else:
#                 code += alphabet.upper()[alphabet.upper().index(i) - 13]
#         else:
#             code += i
#     return code
#
# code = rot13(text)
#
# print(code)
#
# encode = rot13(code)
#
# print(encode)
