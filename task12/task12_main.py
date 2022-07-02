# coding=utf-8
"""

Напишите функцию, которая принимает список списков и возвращает значение всех символов в нем,
где каждый символ добавляет или отнимает что-то от общего балла. Значения символов:
# = 5
О = 3
Х = 1
! = -1
!! = -3
!!! = -5
Если итоговый результат отрицательный, верните 0
(например, 3 #, 3 !!, 2 !!! и X будет (5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) = -3, так что верните 0.
"""

characters = {
    '#': 5,
    'О': 3,
    'X': 1,
    '!': -1,
    '!!': -3,
    '!!!': -5
}


def test_function(combination: list) -> int:
    result = sum([characters[x[1]] * x[0] for x in combination])
    if result < 0:
        return 0
    return result


print(test_function([[3, '#'], [3, '!!'], [2, '!!!'], [1, 'X']]))
print(test_function([[4, '#'], [3, '!!'], [2, '!!!'], [1, 'X']]))