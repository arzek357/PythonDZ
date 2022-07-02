# coding=utf-8
"""
Написать функцию, которая будет приниметь одно значение с логическими типы,
а затем ковертировать их в строковые 'True' и 'False' и возвращать эти значения.
"""


def bool_to_string(condition: bool) -> str:
    return str(condition)


print(bool_to_string(False))
print(bool_to_string(True))