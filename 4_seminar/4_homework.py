# 1. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

# import itertools
# from itertools import combinations
#
# array = [1, 5, 2, 3, 4, 6, 1, 7]
# for i in range(len(array)-1):
#     possible_comb = list(combinations(array, len(array)-i))
#     for j in range(len(possible_comb)-1):
#         result = list(possible_comb[j])
#         if result == sorted(result):
#             print(result)

# 2.	Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

# import random
# from random import randint
#
# file = 'file_from_task_2.txt'
# array = []
# with open(file, 'w') as data:
#     for i in range(0, 10):
#         array.append(random.randint(-100, 101))
#     data.write(str(sorted(array)))



# 3.	Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0.
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).

# file = '1Kints.txt'
# array = []
# sum = 0
# data = open(file, 'r')
# for line in data:
#     s = int(line)
#     array.append(s)
#
#
# for i in range(len(array)-1):
#     for j in range(len(array)-2):
#         for k in range(len(array)-3):
#             if (array[i]+array[j]+array[k] == 0):
#                 print(f'{array[i]} + {array[j]} + {array[k]}')
#
