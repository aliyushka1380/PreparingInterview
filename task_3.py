"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.

Пример:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23, 'elem_19': 19, 'elem_16': 16, 'elem_8': 8}
)


even, odd = 0, 0

def palindrom(s, r):
    global even, odd
    if len(s) <= 0:
        return even, odd

    else:
        if int(s[0]) % 2 == 0:
            even += 1
            return f'{even} {palindrom(s[1:])}'
        else:
            odd += 1
            return f'{odd} {palindrom(s[1:])}'


a = input('Введите начальное число генерации: ')
r = input('Введите конечное число генерации: ')

palindrom(a, r)
print(f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})')
"""

from random import randint
new_tuple = []
new_list = [randint(1, 100) for i in range(10)]
new_tuple.append(new_list)
new_dict={}
for i in new_list:
    new_dict[f"{'elem_'}{i}"] = i
new_tuple.append(new_dict)
print(tuple(new_tuple))

