# coding=utf-8
"""
Напишите функцию, которая принимает два значения - числа num, length (основное число, количество умножений).
Функция должна возвращать список перемножений числа num length раз.
Пример: test_function(7, 5) ➞ [7, 14, 21, 28, 35]
"""


def test_function(num: int, length: int) -> list:
    return [num*x for x in range(1, length+1)]


print(test_function(7, 6))
