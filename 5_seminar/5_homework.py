# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

# Решение
# delete = 'абв'
# line = 'абвгдеж раВав копыто фабв абв АбВжэжд Абкн абрыволк аБволк'
#
# new_line = line.lower()
# filtered_line = new_line.replace('абв', '')
#
# print("Отфильтрованная строка:", filtered_line)

# 2
# delete = 'абв'
# line = 'абвгдеж рабав копыто фабв абв АбВжэжд Абкн абрыволк аБволк'
#
# split_line = line.split()
# # print(split_line)
# filtered_line = ' '.join((filter(lambda s: s not in delete, line)))
#
# print("Отфильтрованная строка:", filtered_line)

# 3
# def find_all_indexes(enter, search):
#     line = []
#     length = len(enter)
#     index = 0
#     while index < length:
#         i = enter.find(search, index)
#         if i == -1:
#             return line
#         line.append(i)
#         index = i + 1
#     return line
# s = 'абвгдеж рабав копыто фабв абв АбВжэжд Абкн абрыволк аБволк'
#
# new_arr = sorted(find_all_indexes(s, 'абв'), reverse=True)



# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.





# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче.
# Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе,
# жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе,
# ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой
# дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.
#
import re

# file = '«Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил»'
# bad_word = ['ну', 'в общем', 'короче', 'короче говоря', 'кажется', 'эээ', 'эээээ…', 'кстати', 'ээээ…', 'как бы', 'ясен пень']
# line = file.lower()
#
# a = re.sub(r'(короче говоря|[,\[\]])', '', line)
# s = re.sub(r'(ну|[,\[\]])', '', a)
# f = re.sub(r'(в общем|[,\[\]])', '', s)
# g = re.sub(r'(короче|[,\[\]])', '', f)
# h = re.sub(r'(кажется|[,\[\]])', '', g)
# j = re.sub(r'(ясен пень|[,\[\]])', '', h)
# k = re.sub(r'(кстати|[,\[\]])', '', j)
# l = re.sub(r'(как бы|[,\[\]])', '', k)
# q = re.sub(r'(эээээ…|[,\[\]])', '', l)
# w = re.sub(r'(ээээ…|[,\[\]])', '', q)
# r = re.sub(r'(эээ…|[,\[\]])', '', w)
# t = re.sub(r'(эээ|[,\[\]])', '', r)
# print(t)
#
#
