"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.

Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Например:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
и
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Например:
91 zmsebjvdgi

42 ychpwljtzn

...

Первая функция должна возвращать ссылку на файловый дескриптор


После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
"""
"""
def prepare_file():

    spam = 'text.txt'
    text_list = [chr(i) for i in range(97, 123)]

    print(chr(91))
    print(ord('A'))
    print(ord('Z'))

    # pass

prepare_file()
"""

import os

def create_file():
    file_name = input("Name: ")
    if os.path.isfile(file_name):
        print('Файл с таким именем уже существует')
    else:
        # list_first = [91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
        list_first = [_ for _ in range(10)]
        # list_second = ['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp', 'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']
        list_second = [_ for _ in 'asjkencbjsdmnvijKJNiwnweijw']
        with open(file_name, 'w') as f:
            for num, text in zip(list_first, list_second):
                f.write(str(num) + '  ' + text + '\n')
        return file_name

def read_file():
    file_name = create_file()
    with open(file_name) as f:
        return f.readlines()

print(read_file())