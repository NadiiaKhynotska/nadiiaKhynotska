#
# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# def select_numbers(string):
#     numbers = [i for i in string if i.isdigit()]
#     return ','.join(numbers)
#
#
# string = input('Enter a string: ')
# result = select_numbers(string)
# print(result)


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# def select_nums(string):
#     word_list = string.split(' ')
#     nums = [word for word in word_list if word.isdigit()]
#     return ','.join(nums)
#
#
# string_input = input('Enter a string: ')
# result = select_nums(string_input)
#
# print(result)
# #################################################################################
#
# list comprehension
#
# 1)є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
new_greeting = [i.upper() for j in greeting.split() for i in j]
print(new_greeting)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
print([i ** 2 for i in range(50) if i % 2 != 0])


# function
#
# - створити функцію яка виводить ліст
def generate_list(num):
    print([i for i in range(num)])


generate_list(45)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def get_max_num(a, b, c):
    max_num = max(a, b, c)
    print(f'Max num is {max_num}')
    return max_num


max_num = get_max_num(34, -3, 12)
print(max_num)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def get_min_max_num(*args):
    min_num = min(args)
    max_num = max(args)
    print(f'Max num is {max_num}')
    return min_num


min_num = get_min_max_num(34, 23, -23345, 234455)
print(min_num)


# - створити функцію яка повертає найбільше число з ліста
def get_max_num_from_list(list):
    if not list:
        return None
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num = num
    return max_num


my_list = [23455, 3, 5, 78]
max_num = get_max_num_from_list(my_list)
print(f'Max num is {max_num}')


# - створити функцію яка повертає найменьше число з ліста
def get_min_num_from_list(list):
    if not list:
        return None
    min = list[0]
    for num in list:
        if num < min:
            min = num
    return min


my_list = [23455, 3, 5, 78]
min_num = get_min_num_from_list(my_list)
print(f'Min num is {min_num}')


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def get_sum_from_list(list):
    if not list:
        return None
    sum = 0
    for num in list:
        sum += num
    return sum


my_list = [20, 30, 50, 78]
sum = get_sum_from_list(my_list)
print(f'Sum is {sum}')


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def get_avg(list):
    if not list:
        return None
    sum = 0
    for num in list:
        sum += num
    return sum / len(list)


my_list = [20, 30, 50, 78]
avg = get_avg(my_list)
print(f'Avg is {avg}')
#
#
#
#
# ################################################################################################
# 1)Дан list:
list = [22, 3, 5, 2, 8, 2, -234, 8, 23, 5, 22]
#   - знайти мін число
min_number = min(list)
print(f'Min num is {min_number}')
#   - видалити усі дублікати
uniq_list = set(list)
print(f'Uniq list is {uniq_list}')
#   - замінити кожне 4-те значення на 'X'
for i in range(3, len(list), 4):
    list[i] = 'X'

print(f'Changed list is {list}')


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def print_square(side):
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1 or j == 0 or j == side - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


square_side = int(input("Enter the length of the square side: "))
print_square(square_side)


# 3) вывести табличку множення за допомогою цикла while
def print_multiplication_table():
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            print(f"{i} x {j} = {i * j}")
            j += 1
        i += 1
        print()


print_multiplication_table()


def print_pifagor_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:3}", end=" ")
        print()


print_pifagor_table()

# 4) переробити це завдання під меню
