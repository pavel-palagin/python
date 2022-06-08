#Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях. Позиции хранятся
# в файле file.txt в одной строке одно число
import random
from random import randint
#
# N = int(input("Введите N: "))
# array = []
#
#
# for i in range(N):
#     array.append((random.randint(-N, N)))
# print(array)
#
# with open('file.txt', 'w') as data:
#     for i in range(N//2):
#         data.write(f'{randint(0,N-1)}\n')
#
# data = open('file.txt', 'r')
# res = 1
# for line in data:
#     res = res * array[int(line)]
#     print(line)
# print(res)


# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

# from random import randint
#
# N = int(input('Введите N: '))
# myList = []
# path = 'file.txt'
# for i in range(N):
#     j = randint(-N, N)
#     myList.append(j)
# print(myList)
#
# with open(path, 'w') as data:
#     for i in range(N//2):
#         data.write(f'{randint(0,N-1)}\n')
#
# data = open(path, 'r')
# proizv = 1
# for line in data:
#     proizv *= int(myList[int(line)])
# print(proizv)








#Дано число. Составить список чисел Фибоначчи, в том числе для
# отрицательных индексов.  Т е для k = 8, список будет выглядеть
# так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#
# N = int(input("Введите N: "))
# array = []
#
# def fib(N):
#     if N in [1,2]:
#         return 1
#     else:
#         return fib(N-1) + fib(N-2)
#
# for i in range (N):
#     array

# Дано число. Составить список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так:
# [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibo(n):
    if n>=0:
       idx = range(n+1)
       x = [0,1]
       for k in idx[2:]:
           x.append(x[k-1] + x[k-2])
       return x[n]
    else:
       n=-(n-1)
       idx = range(n+1)
       x = [1,0]
       for k in idx[2:]:
           x.append(x[k-2] - x[k-1])
       x.reverse()
    return x[0]

k=int(input('Введите число: '))
for i in range(-k,k+1):
    print(fibo(i), end=" ")




#Строка содержит набор чисел. Показать большее и меньшее число Символ-разделитель - пробел



#Найти корни квадратного уравнения Ax² + Bx + C = 0
