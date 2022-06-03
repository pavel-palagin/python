# 1.	Найти сумму чисел списка стоящих на нечетной позиции (нечетный индекс или нечетный по счету?)
#
import random
N = int(input("Введите количество элементов в списке: "))
list = []
sum1 = 0    #сумма для элементов стоящих на нечетных индексах
sum2 = 0    #сумма для элементов стоящих на нечетных позициях
for i in range(1, N+1):
    list.append(random.randint(0, 10))

print(list)

for i,numbers in enumerate(list):
    if i % 2 != 0:
        sum1 = sum1 + numbers
print(sum1)

for i,numbers in enumerate(list):
    if i % 2 == 0:
        sum2 = sum2 + numbers
print(sum2)

# 2.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

# import random
# N = int(input("Введите количество элементов в списке: "))
# array = []
#
# for i in range(1, N+1):
#     array.append(random.randint(0, 10))
#
# print(array)
#
# for i, numbers in enumerate(array):
#     if i <= N//2:
#         result = array[i]*array[N-i-1]
#         # print(result, end = ' ')
#         print(f"{array[i]} * {array[N-i-1]} = {result}")


# 3.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# array = []

# for i in range(0, 5):
#     array.append(round(random.random()*10, 2))
# print(array)

# new = []
# for i, numbers in enumerate(array):
#     a = array[i] % 1
#     new.append(round(a,2))
# print(new)

# max = 0
# min = new[0]
# for i, numbers in enumerate(new):
#     if new[i] > max:
#         max = new[i]
#     if new[i] < min:
#         min = new[i]

# print(f"Разница между максимальным {max} и минимальным {min} значением дробной части элементов списка {array} равна {round(max-min,2)}")


# 4.	Написать программу преобразования десятичного числа в двоичное

# N = int(input("Введите число: "))
# bin = []
# while N > 0:
#     a = N % 2
#     N = N // 2
#     bin.append(a)
# bin.reverse()
# print(bin)

# N = int(input("Введите число: "))
# a = ''
# while N > 0:
#     a = str(N % 2) + a
#     N = N // 2
# print(a)
