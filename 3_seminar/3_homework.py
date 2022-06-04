# 1.	Найти НОК двух чисел
# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))
#
# for i in range(1, 10000):
#     if (i % first == 0 and i % second == 0):
#         print(f'Наименьшее общее кратное чисел {first} и {second} равно {i}')
#         break

# 2.	Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.

# d = input("Введите необходимую точность: ")
#
# list = d.split('.')
# part = list[1]
# s = len(part)
#
# # ряд Нилаканта, π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)
# pi = 3
# x = 2
# y = 3
# z = 4
# for i in range(100000):
#     pi += 4 / (x * y * z)
#     x += 2
#     y += 2
#     z += 2
#     pi -= 4 / (x * y * z)
#     x += 2
#     y += 2
#     z += 2

# ряд Лейбница π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...

# pi = 0
# x = 1
#
# for i in range(100000):
#     pi += 4 / (x)
#     x += 2
#     pi -= 4 / (x)
#     x += 2
#
# print(pi)
# print(round(pi, s))


# 3.	Составить список простых множителей натурального числа N
# N = int(input("Введите число: "))
# array = []
# i = 2
# while N > 1:
#     if N % i == 0:
#         N = N // i
#         array.append(i)
#     else:
#        i += 1
# print(array)



# 4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# import random
# array = []
# for i in range(0, 10):
#     array.append(random.randint(0, 10))
# print(array)
# array = set(array)
# print(array)



# + на тему файловой системы:
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

# file = 'task_5_from_homework.txt'
#
# newFile = 'newFile.txt'
#
# def readData(file):
#     data = open(file, 'r')
#     for line in data:
#         s = line
#     data.close()
#     return s
#
# array = list(map(int, readData(file).split()))
# print(array)
# print()
#
# new = []
# for numbers in array:
#     if numbers % 2 == 0:
#         new.append(numbers)
# print(new)
#
# with open(file, 'w') as data:
#     data.write(str(new))
















