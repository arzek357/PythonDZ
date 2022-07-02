# coding=utf-8
"""
Написать функцию, которая будет принимать одно значение - строку.
Функция определяет свободные и занятые участки пляжа.
Строка состоит из двух символов 0 - свободный участок, 1 - занятый участок.
Из-за недавних ограничений новый человек не может занять место рядом с другим.
Должно быть одно свободное место между двумя людьми, отдыхающими на пляже.
Функци должна вернуть число - количество новых людей, которые могут воспользоваться местами на пляже.
"""


def test_function(places: str) -> int:
    result = 0
    counter = 0
    for place in places:
        if place == '0' and counter == 0 and :

        elif place == '0' and (places[counter - 1] + places[counter + 1] == 0):
            result += 1


    return result
