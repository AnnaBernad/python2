#strings1.2

# str = input()
# num_list = []
# num = ""
# for i in str:
#     if i.isdigit():
#         num = num + i
#     else:
#         if num != '':
#             num_list.append(int(num))
#         num = ''
# if num != '':
#     num_list.append(int(num))
#
# print(num_list)

#list comprehension2.1

# greeting = 'Hello, world'
# greet2 = greeting.upper()
# sep = [i for i in greet2]
# print(sep)

#2.2

# l1 = [i for i in range(51)]
# print(l1)
# l2 = [ i**2 for i in l1 if i%2 ==1]
# print(l2)

#function

# - створити функцію яка виводить ліст

# l = []
#
#
# def create_l(a, b, c, d, e):
#     l1 = [a, b, c, d, e]
#     print(l1)
#
#
# map_list = map(create_l, l)
# create_l(1, 2, 3, 4, 5)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# a = input()
# b = input()
# c = input()
#
#
# def min_num(a, b, c):
#     l = [a, b, c]
#     print(min(l))
#     return
#
#
# if (a != None and b != None and c != None):
#     map_list = map(min_num, a, b, c)
#     min_num(a, b, c)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# a = input()
# b = input()
# c = input()
#
#
# def max_num(a, b, c):
#     l = [a, b, c]
#     print(max(l))
#     return
#
#
# if (a != None and b != None and c != None):
#     map_list = map(max_num, a, b, c)
#     max_num(a, b, c)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# - створити функцію яка повертає найбільше число з ліста

# l = [16, 56, 79, 1, 567]
# #
# #
# # def create_l(x):
# #     l = max(x)
# #     print(l)
# #     return
# #
# #
# # map_list = map(create_l, l)
# # create_l(l)

# - створити функцію яка повертає найменьше число з ліста

# l = [16, 56, 79, 1, 567]
#
#
# def create_l(x):
#     l = min(x)
#     print(l)
#     return
#
#
# map_list = map(create_l, l)
# create_l(l)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення


def decor(func):
    def wrap(**kwargs):
        x = ""
        func(**kwargs)
        x = x.replace("_", " ")
        print(x)

    return wrap


@decor
def pr():
    print('Hello_boss_!!!')

pr()

