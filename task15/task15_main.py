"""
Создайте функцию, которая определяет, может ли c каждого места в концертном заде видеть сцену.
С места можно увидеть сцену, если значение этого места (указано во входном списке) строго больше, чем значение перед ним.
Каждый может увидеть сцену в примере ниже:

[[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], [5, 5, 5, 5, 4, 4], [6, 6, 7, 6, 5, 5]]

Не все видят сцену:

[[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], [5, 5, 5, 10, 4, 4], [6, 6, 7, 6, 5, 5]]

Функция должна возвращать True, если абсолютно все видят сцену, ичане False
"""
from typing import Union, List


def test_function(rows: list) -> bool:
    result = True
    previous_row = []
    for row in rows:
        if len(previous_row) == 0:
            previous_row = row
            continue
        for i in range(0, len(row) - 1):
            if previous_row[i] > row[i]:
                result = False
                break
        if not result:
            break
    return result


print(test_function([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], [5, 5, 5, 5, 4, 4], [6, 6, 7, 6, 5, 5]]))
