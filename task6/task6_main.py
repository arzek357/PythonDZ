# coding=utf-8
"""
Напишите функцию, которая принимает одно значение - число .
Функция должна возвращать строку - полученное число в двоичном виде
"""


def convert_number(number: int) -> str:
    return str(bin(number))[2:]


print(convert_number(11))
