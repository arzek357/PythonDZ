# coding=utf-8
"""
Написать функцию, которая будет принимать одно значение - список.
Функция должна возвращать самое частое значение в списке (встречается > N/2).
Пример: test_function(["A", "A", "A", "B", "C", "A"]) ➞ "A"
"""


def test_function(values: list):
    dictionary = {}
    counter = 0
    result = None

    for item in values:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
            if dictionary[item] > counter:
                result = item
                counter = dictionary[item]

    if counter > len(values) / 2:
        return result
    else:
        print("Самое частое значение в спике не удовлетворяет требованию >N/2!")
    return None


print(test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 'A', 3, 44, 44, 44, 44, 44, 44]))
print(test_function(['A', 'A', 2]))
print(test_function(['A', 'A', 2, 2, 3]))
