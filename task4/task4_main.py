# coding=utf-8
"""
Написать функцию, которая будет принимать одно значение - число.
Функция должна возвращать список всех четных чисел в диапозоне от 1 до полученного числа.
В этом задании нужно использовать list comprehension.
"""


def get_numbers(number: int) -> list:
    return [x for x in range(2, number, 2)]

print(get_numbers(13))
