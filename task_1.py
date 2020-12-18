"""
1. Написать программу, которая будет содержать функцию
для получения имени файла из полного пути до него.

При вызове функции в качестве аргумента должен передаваться путь до файла.
В функции необходимо реализовать «выделение» из этого пути имени файла (без расширения).

Пример:
функция принмает следующую строку - '../mainapp/views.py'

Результат:
views
"""


from os import path

def file_name(path_file):
    part_path = path.basename(path_file)
    split_text = path.splitext(part_path)[0]
    return split_text

print(file_name('../mainapp/views.py'))