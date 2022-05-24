#1. Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

# N = int(input("Введите число: "))

# for i in range (0, N+1):
#     row = (-3)**i
#     print(f"{i}: {row}")



#2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# N = int(input("Введите число: "))

# for i in range (1, N+1):
#     row = 3*i +1
#     print(f"{i}: {row}", end = ', ')
    


#3. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# string_1 = 'список'
# string_2 = 'Сформировать список из N членов последовательности'
# counter = string_2.count(string_1)
# print(counter)


#4. Подсчитать сумму цифр в вещественном числе.

# import random
# n = round(random.random()*100, 5)
# print(f"Случайное вещественное число: {n}")
# string = str(n)
# list = string.split('.')
# integerPart = int(list[0])
# doublePart = int(list[1])
# print(f"Целая часть вещественного числа: {integerPart}")
# print(f"Дробная часть вещественного числа: {doublePart}")
# sum_int = 0
# sum_double = 0
# while integerPart > 0:
#     sum_int = sum_int + integerPart%10
#     integerPart = integerPart//10

# while doublePart > 0:
#     sum_double = sum_double + doublePart%10
#     doublePart = doublePart//10

# print(f"Сумма цифр целой части вещественного числа: {sum_int}")
# print(f"Сумма цифр дробной части вещественного числа: {sum_double}")
# print(f"Сумма всех цифр вещественного числа: {sum_int + sum_double}")






#5. Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ].

# N = int(input("Введите число: "))

# factorial = 1
 
# for i in range(1, N+1):
#     factorial *= i
#     print(factorial, end = ' ')

