# coding=utf-8
"""
Написать функцию, которая будет приниметь одно значение - список.
Вычислить разницу между максимальным и минимальным значением и вернуть его.
"""


def max_min_difference(values: list):
    return max(values) - min(values)


print(max_min_difference([1, 2, 3, 4, 5, 6, 7]))
