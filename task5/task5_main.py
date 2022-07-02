# coding=utf-8
"""
Напишите функцию, который имеет два аргумента - x и y.
Функция должна выводить координатный угол, в котором находятся координаты (x, y).
Точки внутри координатного угла I имеют положительные абсциссы и ординаты.
Точки внутри координатного угла II имеют отрицательные абсциссы и положительные ординаты.
Точки внутри координатного угла III имеют отрицательные абсциссы и ординаты
Точки внутри координатного угла IV имеют положительные абсциссы и отрицательные ординаты.
"""


def get_coordinate_angle(x: int, y: int):
    if x > 0:
        if y > 0:
            print("Точка находится в координатном угле I.")
        if y < 0:
            print("Точка находится в координатном угле IV.")
    elif x < 0:
        if y > 0:
            print("Точка находится в координатном угле II.")
        if y < 0:
            print("Точка находится в координатном угле III.")
    else:
        print("Точка лежит на одной из осей координат.")


get_coordinate_angle(0, -1)
get_coordinate_angle(1, -1)